"""
    多态：一个抽象类有多个子类，不同子类重写父类的方法，呈现多种执行效果
"""


# 父类
class Dog(object):
    def work(self):  # 父类提供统一的方法，哪怕是空方法
        print('指哪打哪...')


class ArmyDog(Dog):  # 继承Dog类
    def work(self):  # 子类重写父类同名方法
        print('追击敌人...')


class DrugDog(Dog):
    def work(self):
        print('追查毒品...')


class Person(object):
    def work_with_dog(self, dog):  # 传入不同的对象，执行不同的代码，即不同的work函数
        dog.work()


ad = ArmyDog()
dd = DrugDog()
daqiu = Person()
daqiu.work_with_dog(ad)  # 追击敌人...
daqiu.work_with_dog(dd)  # 追查毒品...
