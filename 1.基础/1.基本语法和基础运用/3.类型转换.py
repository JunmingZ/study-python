"""
    int()
    float()
    str()
    list()
    tuple()
    eval()
"""

num1 = 1
print(float(num1), type(float(num1)))  # 1.0 <class 'float'>

print('-' * 20)
# ------------------------------------------


num2 = 10
print(type(str(num2)))  # <class 'str'>

print('-' * 20)
# ------------------------------------------


# tuple() -- 将一个序列转换成元组
list1 = [10, 20, 30]  # 列表
print(tuple(list1), type(tuple(list1)))  # (10, 20, 30) <class 'tuple'>

print('-' * 20)
# ------------------------------------------


t1 = (100, 200, 300)  # 元组
print(list(t1), type(list(t1)))  # [100, 200, 300] <class 'list'>

print('-' * 20)
# ------------------------------------------
# 将字符串串中的数据转换成Python表达式原本类型
str1 = '10'
str2 = '[1, 2, 3]'
str3 = '(1000, 2000, 3000)'
str4 = '{1,2,3}'
print(type(eval(str1)))   # <class 'int'>
print(type(eval(str2)))   # <class 'list'>
print(type(eval(str3)))   # <class 'tuple'>
print(type(eval(str4)))   # <class 'set'>

