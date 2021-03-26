import pymysql.cursors


def get_connect():
    connect = pymysql.connect(host='127.0.0.1',
                              port=3306,
                              user='autotest',
                              passwd='password',
                              db='test_db',
                              charset='utf8',
                              autocommit=True)  # db:表示数据库名称
    return connect


# 查询数据
def query(sql):
    connect = get_connect()
    # 获取游标
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    result_data = cursor.fetchone()
    result.pop('id')
    result.pop('expected')
    cursor.close()
    connect.close()
    return result_data


# 更新数据
def update(sql):
    connect = get_connect()
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    result_new_date = cursor.execute(sql)
    cursor.close()
    connect.close()
    return result_new_date


# 删除数据
def delete(sql, args):
    connect = get_connect()
    cur = connect.cursor()
    result_delete = cur.execute(sql, args)
    cur.close()
    connect.close()
    return result_delete


if __name__ == "__main__":
    result = update("UPDATE `create_shop_staff` set department_id=43534 where id=1;")
    print(result)
