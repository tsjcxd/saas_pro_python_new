import pymysql.cursors
from pymysql.cursors import DictCursor

from conf import test_db_info


class DB:
    def __init__(self, db_config=None):
        if db_config is None:
            self.db_config = test_db_info
        else:
            self.db_config = db_config
        self.conn = self.get_connect()
        self.cursor = self.conn.cursor()

    def get_connect(self):
        connect = pymysql.connect(**self.db_config, autocommit=True, cursorclass=DictCursor)  # db:表示数据库名称
        return connect

    def close(self):
        self.cursor.close()
        self.conn.close()

    # # 查询数据
    # def query(self, sql):
    #     # 获取游标
    #     self.cursor.execute(sql)
    #     return self.cursor.fetchone()

    def execute(self, sql):
        result = self.cursor.execute(sql)
        return result

    def get_fetchone(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        result.pop('id')
        result.pop('comments')
        result.pop('expected')
        return result



if __name__ == "__main__":
    db = DB()
    result = db.get_fetchone(sql="SELECT * FROM create_shop_staff WHERE id=1;")
    print(result)
