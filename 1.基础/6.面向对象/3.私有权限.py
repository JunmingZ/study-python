class Master(object):
    def __init__(self):
        self.name = '师傅'
        # 私有属性
        self.__money = 10000

    def print_info(self):
        print(f'{self.name} 有 {self.__money} 元')

    # 获取私有属性
    def get_money(self):
        return self.__money

    # 修改私有属性
    def set_money(self, money):
        self.__money = money

    # 私有方法
    def __info_print(self):
        print(self.name)
        print(self.__money)


master = Master()
master.print_info()  # 师傅 有 10000 元

try:
    print(master.__money)
except Exception as e:
    print(e)  # 'Master' object has no attribute '__money'

# 实例对象无法获取私有属性和私有方法
