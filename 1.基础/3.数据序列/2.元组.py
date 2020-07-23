"""
    index()：查找某个数据，如果数据存在返回对应的下标，否则报错，语法和列表、字符串的index方法相同。
    count() 和列表相同
    len()：统计元组中数据的个数(和列表相同)
"""
print('-' * 20, 'index')
tuple1 = ('aa', 'bb', 'cc', 'bb')
print(tuple1.index('aa'))  # 0


# ------------------------------------------------------
print('-' * 20, '尝试删除')
# 尝试使用删除
tuple1 = ('aa', 'bb', 'cc', 'bb')

try:
    del tuple1[0]
except Exception as result:
    print(result)  # 'tuple' object doesn't support item deletion

# ------------------------------------------------------

print('-' * 20, '尝试赋值后修改')
tuple1 = ('aa', 'bb', 'cc', 'bb')

a = tuple1
try:
    a[0] = 1
except Exception as e:
    print(e)  # 'tuple' object does not support item assignment
