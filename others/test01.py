
[{'id': 588, 'name': '未分类部门', 'children': [], 'count': 38}, {'id': 252, 'name': '销售部', 'children': [], 'count': 96}, {'id': 253, 'name': '教练部', 'children': [{'id': 1021, 'name': '教练一部', 'children': [], 'count': 4}], 'count': 151}, {'id': 262, 'name': '数据域部门', 'children': [{'id': 263, 'name': '1号部门', 'children': [{'id': 264, 'name': '2好部门', 'children': [], 'count': 5}], 'count': 9}, {'id': 265, 'name': '3号部门', 'children': [], 'count': 22}], 'count': 37}, {'id': 285, 'name': '全量回归测试部', 'children': [], 'count': 12}, {'id': 287, 'name': '轻嘤部门', 'children': [], 'count': 12}, {'id': 288, 'name': '数据域部门A', 'children': [{'id': 289, 'name': '数据域部门AA', 'children': [{'id': 291, 'name': '数据域部门AAA', 'children': [], 'count': 6}], 'count': 13}, {'id': 290, 'name': '数据域部门AB', 'children': [], 'count': 6}], 'count': 25}, {'id': 294, 'name': 'lite版人脸部门', 'children': [], 'count': 3}, {'id': 377, 'name': 'Pro回归专用（勿动）', 'children': [], 'count': 4}, {'id': 386, 'name': '一级部门', 'children': [{'id': 387, 'name': '一级部门子部门', 'children': [], 'count': 1}], 'count': 2}, {'id': 833, 'name': '新部门', 'children': [{'id': 834, 'name': '嗯嗯', 'children': [{'id': 835, 'name': '汤汤', 'children': [{'id': 836, 'name': '预约', 'children': [{'id': 837, 'name': '一条', 'children': [], 'count': 3}], 'count': 3}], 'count': 3}], 'count': 3}], 'count': 3}]


department = [{'a': 1, 'b': 2}, {'a': 11, 'b': 22}, {'a': 111, 'b': 222}]


dict1 = {}

for d in department:
    dict1.update(d)
    print(dict1)


