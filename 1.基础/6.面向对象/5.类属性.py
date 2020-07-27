"""
    类属性：该类的所有实例对象所共有，仅占用一份内存
    修改只能通过类对象修改，不能通过实例对象，若是通过实例对象则是创建一个实例属性
    和类方法搭配使用，类方法可以修改类属性，类似java的static
"""


class Dog(object):
    tooth = 10

    def set_tooth(self, num):
        self.tooth = num

    # 声明类方法
    @classmethod
    def set_class_tooth(cls, num):
        """
        :cls 类对象
        :param num:
        :return:
        """
        cls.tooth = num


wangcai = Dog()
xiaohei = Dog()

# 创建了一个实例对象
wangcai.tooth = 20
# 修改类属性
Dog.tooth = 12

print(Dog.tooth)  # 12
print(wangcai.tooth)  # 20
print(xiaohei.tooth)  # 12

# -------------------------------------------------
print('-' * 30, '通过方法修改')
# 通过方法修改
xiaohei.set_tooth(15)

print(Dog.tooth)  # 12
print(wangcai.tooth)  # 20
print(xiaohei.tooth)  # 15

# 无法修改，因为方法中使用self是代表该类的实例，所以只是创建了实例属性


# -------------------------------------------------

print('-' * 30, '通过类方法修改')

xiaohei.set_class_tooth(30)
print(Dog.tooth)  # 30
print(wangcai.tooth)  # 20
print(xiaohei.tooth)  # 15

# 修改成功
