"""
   一个类只能有一个构造函数
"""


class Washer:
    """
        __init__: 构造函数
        self 代表类的实例
    """

    def __init__(self, width, height):
        # 实例属性
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽度是{self.width},洗衣机的高度是{self.height}')

    """
        默认打印对象的内存地址,
        使用__str__(self) 就会打印从在这个方法中 return 的数据
    """
    def __str__(self):
        return '这是一个洗衣机类'

    """
        析构函数，释放对象时使用
    """
    def __del__(self):
        print(f'{self}对象已经被删除')


# 创建对象
washer = Washer(10, 20)
washer.print_info()  # 洗衣机的宽度是10,洗衣机的高度是20
print(washer)  # 执行__str__(self)： 这是一个洗衣机类

del washer  # 这是一个洗衣机类对象已经被删除
