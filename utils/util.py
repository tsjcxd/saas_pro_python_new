import random
import datetime
import time


def random_name(num, prefix=''):
    h = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄和穆萧尹姚邵堪汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁'
    if len(prefix) > num:
        digt = 0
    else:
        digt = num - len(prefix)
    name = prefix + ''.join(random.sample(h, digt))
    return name


def random_phone():
    phonelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                 "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                 "186", "187", "188", "189"]
    return random.choice(phonelist) + "".join(random.choice("0123456789") for i in range(8))


def get_time():
    now = time.time()
    return int(round(now * 1000))


def get_date(day):
    today = (datetime.datetime.now()+datetime.timedelta(days=day)).strftime('%Y-%m-%d')
    return today


if __name__ == '__main__':
    a = random_name(5, "员工")
    print(a)
