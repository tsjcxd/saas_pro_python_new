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
#     result = database_operate("SELECT count(*) as total_num FROM `personal_course_template` where publish_channel=1 and is_del=0 and is_available=1 and brand_id=273567221088319;")
#     # for item in result:
#     print(result)
#     # print(type(result))
#     # print(type(result['total_num']))
