import random

def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
    val = f'{head:x}{body:x}'
    st = bytes.fromhex(val).decode('gb2312')
    return st

def create_name():
    n = random.randint(1, 2)
    name = ''
    for i in range(n):
        s = GBK2312()
        name = name+s
    return first_name()+name