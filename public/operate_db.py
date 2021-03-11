import os
import pymysql
from pymysql.cursors import DictCursor
from sshtunnel import SSHTunnelForwarder


# class OperateDatabase:
def database_operate(sql):
    KEY_FILE = "C:\\Users\\EDZ\\.ssh\\id_rsa"
    server = SSHTunnelForwarder(
        ssh_address_or_host=('101.132.119.70', 22), # 指定ssh登录的跳转机的address
        ssh_username='tangsaijuan', # 跳转机的用户
        ssh_pkey=KEY_FILE,
        remote_bind_address=('rm-uf61485wcg7578wl3.mysql.rds.aliyuncs.com', 3306)
    )  
    server.start()


    db = pymysql.connect(
        host='127.0.0.1',
        port=server.local_bind_port,    #默认
        user="tangsaijuan",                    
        password="UT9rCy05R0Vd",
        database="saas_test"
        )

    try:
        cur = db.cursor(pymysql.cursors.DictCursor)    
        cur.execute(sql)
        data = cur.fetchall()
        return data
    except:
        print("数据库连接失败")
    db.close()

    server.stop()

if __name__== "__main__":
    result = database_operate("SELECT count(*) as total_num FROM `personal_course_template` where publish_channel=1 and is_del=0 and is_available=1 and brand_id=273567221088319;")
    # for item in result:
    print(result)
    # print(type(result))
    # print(type(result['total_num']))
