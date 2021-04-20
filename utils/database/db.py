import pymysql.cursors
from pymysql.cursors import DictCursor
from sshtunnel import SSHTunnelForwarder
from conf import ssh_info


class DB:
    def __init__(self, db_info=None, is_test_db=True):
        self.db_config = db_info
        if is_test_db:
            self.db_config.update({'port': self.get_ssh_tunnel().local_bind_port})
        print(self.db_config)
        self.conn = self.get_connect()
        self.cursor = self.conn.cursor()

    def get_ssh_tunnel(self):
        server = SSHTunnelForwarder(**ssh_info)
        server.start()
        return server

    def get_connect(self):
        connect = pymysql.connect(**self.db_config,  autocommit=True, cursorclass=DictCursor)  # db:表示数据库名称
        return connect

    def close(self):
        self.cursor.close()
        self.conn.close()

    # # 查询数据
    # def query(self, sql):
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

    def get_fetchall(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result


if __name__ == "__main__":
    from conf import test_db_info, auto_db_info, ssh_info
    db = DB(auto_db_info, False)
    result = db.get_fetchall(sql="show databases;")
    print(result)
