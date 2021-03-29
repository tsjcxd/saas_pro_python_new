

def abc01(a):
    # print(a)
    a = a + 1
    return a


def abc02(func):
    a = 2
    x = func(a)
    return x


if __name__ == '__main__':
    x = abc02(abc01)
    print(x)
