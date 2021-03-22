import pymysql.cursors


def get_data(sql):

    connect = pymysql.Connect(
        host='106.15.229.10',
        port=3306,
        user='auto_test',
        passwd='CZkS7W12',
        db='auto_test',
        charset='utf8'
    )
    # 获取游标
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    # print(cursor)
    cursor.execute(sql)
    result = cursor.fetchone()
    result.pop('id')
    result.pop('expected')
    return result
    cursor.close()
    connect.close()
# if __name__== "__main__":
#     result = get_data("SELECT * FROM `GetBrandShop`;")
#     print(result)
