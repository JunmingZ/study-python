"""
    单继承
"""


class Master(object):
    def __init__(self):
        self.name = '师傅'

    def print_info(self):
        print(f'{self.name} 有 1000 元')


# 继承
class Prentice(Master):
    def __str__(self):
        return '我是徒弟'


# 创建子类对象
prentice = Prentice()
print(prentice)  # 我是徒弟
# 调用父类方法
prentice.print_info()  # 师傅 有 1000 元
