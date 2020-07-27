"""
静态方法既不需要传递类对象也不需要传递实例对象（形参没有self/cls）
通过装饰器 @staticmethod 来进行修饰
取消不需要的参数传递，有利于 减少不必要的内存占用和性能消耗
"""


class Dog(object):
    tooth = 10

    @staticmethod
    def fun2(a):
        print(a)


Dog.fun2(1)  # 1
