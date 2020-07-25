a = 100


def test():
    # global 关键字声明a是全局变量
    global a
    a = 200


test()
print(a)  # 200
