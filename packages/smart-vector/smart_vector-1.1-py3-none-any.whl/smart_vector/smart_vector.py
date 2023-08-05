from smart_chart.common.connect_db import DB_conn
import requests
import json, re
import time
import hashlib


class Text2VecEmbeddingFunction:
    def __init__(self, model_name: str = "shibing624/text2vec-base-chinese"):
        self._model = None
        self.model_name = model_name

    def __call__(self, texts):
        if not self._model:
            import time
            start_time = time.time()
            try:
                from text2vec import SentenceModel
                self._model = SentenceModel(model_name_or_path=self.model_name)
            except ImportError:
                raise ValueError(
                    "The text2vec python package is not installed. Please install it with `pip install text2vec`"
                )
            print(f'load Text2Vec cost: {time.time() - start_time}')
        return self._model.encode(list(texts), convert_to_numpy=True).tolist()  # type: ignore # noqa E501


class Text2VecAPIFunction:

    def __init__(self, appid, token, url):
        self.appid = appid
        self.token = token
        self.url = url
        self.headers = {'Content-type': 'application/json'}

    def __call__(self, texts):
        stamp = int(time.time() * 1000)
        gen_token = f'{self.token}{stamp}{self.appid}'
        signature = hashlib.sha1(gen_token.encode("utf-8")).hexdigest()
        auth_json = {'token': signature, 'stamp': stamp, 'id': self.appid}
        texts = [texts] if isinstance(texts, str) else texts
        data = {"header": auth_json, "text": texts}
        resp = requests.post(self.url, json.dumps(data), headers=self.headers)
        resp.encoding = 'utf-8'
        result = resp.json()
        if result['code'] == 0:
            data = result['data']
        else:
            data = []
        return data


class SmartVectorDB(object):
    def __init__(self, db_config, text_vector, load_host=None, dbtype='starrocks', table='vectors'):
        self._conn = DB_conn()
        self._connect_dict = db_config
        self._connect_dict['dbtype'] = dbtype
        self._text_vector = text_vector
        self._table = table
        if load_host:
            self._load_dict = {**self._connect_dict, 'host': load_host}
        else:
            self._load_dict = None

    def _execute_sql(self, sql):
        return self._conn.execute_sql_list([sql], self._connect_dict)

    def _execute_load(self, contents, table):
        if self._load_dict:
            contents[0][0] = '__' + contents[0][0]
            if self._load_dict['host'].startswith('http'):
                url = self._load_dict['host'] + '/etl/api/upload_file_api/'
                data = {"type": table,
                        "filename": table,
                        "token": self._load_dict['password'],
                        "visitor": self._load_dict['user'],
                        "contents": json.dumps(contents, ensure_ascii=False)
                        }
                # 上传,https可能需要参数 verify=False
                response = requests.post(url, data=data)
                if response.status_code == 200:
                    response = response.json()
                elif response.status_code == 504:
                    response = {"result": "timeout", "data": "Pls wait for mail"}
                else:
                    response = {"result": "error", "data": "some thing wrong"}

                if response['result'] == 'error':
                    raise Exception(response['data'])
            else:
                table = f"{self._connect_dict['db']}.{table}"
                self._conn.insert_contents(contents, table, 100, self._load_dict)
        else:
            table = f"{table}({','.join(contents[0])})"
            contents = contents[1:]
            self._conn.insert_contents_mysql(contents, table, 100, self._connect_dict)

    def _create_table_embeddings(self):
        sql = """
CREATE TABLE IF NOT EXISTS vectors(
    collection String not null,
    sr String,
    id bigint AUTO_INCREMENT,
    embedding Array<Float>,
    document String,
    c String,
    m String,
    owner varchar(50),
    update_time DATETIME DEFAULT CURRENT_TIMESTAMP
)DUPLICATE KEY (collection,sr) comment 'smart embeddings' DISTRIBUTED BY HASH(collection)
"""
        self._execute_sql(sql)

    def _get(self, embedding, where_str, n_results=3, columns='document'):
        # TODO: Starrocks 3.1已加入cosine_similarity_norm函数, 后续看情况加入
        sql = f"""SELECT {columns},array_sum(array_map((x,y)->pow((x-y),2),embedding,{embedding[0]})) as distance FROM {self._table} where {where_str} order by distance limit {n_results}"""
        # sql = f"""SELECT {columns},CosineSimilarity(cast(embedding as string), '{embedding[0]}') as similar FROM vectors where {where_str} order by similar desc limit {n_results}"""
        result = self._execute_sql(sql)
        return result

    def _add(self, collection, sr, documents: list[str], embeddings: list[list[float]],
             categorys: list[str] = None, metadatas: list[dict] = None,
             owners=None, answers: list[str] = None):
        data_to_insert = []
        insert_list = ['collection', 'sr', 'embedding', 'document']
        if categorys:
            insert_list.append('c')
        if metadatas:
            insert_list.append('m')
        if answers:
            insert_list.append('answer')
        if owners:
            insert_list.append('owner')
        for i, embedding in enumerate(embeddings):
            tmp = [
                collection[i] if isinstance(collection, list) else str(collection),
                sr[i] if isinstance(sr, list) else str(sr),
                str(embedding),
                documents[i].replace('\t', ' ').replace('\n', ' ')
            ]
            if categorys:
                tmp.append(str(categorys[i]))
            if metadatas:
                tmp.append(json.dumps(metadatas[i], ensure_ascii=False).replace('\t', ' ').replace('\n', ' '))
            if answers:
                tmp.append(answers[i])
            if owners:
                if isinstance(owners, str):
                    tmp.append(owners)
                else:
                    tmp.append(owners[i])
            data_to_insert.append(tmp)
        data_to_insert = [insert_list] + data_to_insert
        self._execute_load(data_to_insert, self._table)

    def get(self, query):
        query = query.strip()
        if query.startswith('select '):
            return self._execute_sql(query)
        query = re.split('\n+', query)
        where_str = query[1].strip()
        try:
            if not where_str:
                return [['error'], ['need provide where str']]
            embedding = self._text_vector(query[0])
            queryDict = {'embedding': embedding, 'where_str': query[1]}
            if len(query) > 2:
                queryDict['columns'] = query[2]
            if len(query) > 3:
                queryDict['n_results'] = query[3]
        except Exception as e:
            return [['error'], ['query format should be: query_text\nwhere_text\ncolums\n']]
        return self._get(**queryDict)

    def add(self, collection, sr, documents: list, **kwargs):
        embeddings = [self._text_vector(item)[0] for item in documents]
        self._add(collection, sr, documents, embeddings, categorys=kwargs.get('categorys'),
                  metadatas=kwargs.get('metadatas'), owners=kwargs.get('owners'), answers=kwargs.get('answers'))

    def clear(self, collection, owner):
        self._execute_sql(f"delete from {self._table} where collection='{collection}' and owner='{owner}'")
