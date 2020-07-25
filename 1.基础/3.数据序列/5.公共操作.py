"""
    合并 +
    元组 列表 可行
"""

str1 = 'aa'
str2 = 'bb'
str3 = str1 + str2
print(str3)  # aabb

# ---------------------------------------------
"""
    * 复制 字符串、列表、元组
"""
print('-' * 30)

# ---------------------------------------------
"""
    max() 返回容器中元素最大值
    min() 返回容器中元素最小值
"""
print('-' * 30, 'max(),min()')

list1 = [10, 20, 30, 40]
print(max(list1))  # 40
print(min(list1))  # 10

# ---------------------------------------------


""" 
    range(start, end, step) 供for使用 
    start: 起始
    end： 结束
    step: 步长
"""
print('-' * 30, 'range')

for i in range(1, 9, 1):
    print(i, end=' ')  # 1 2 3 4 5 6 7 8
"""
    等同于java
    for(int i = 1; i < 9; i++)
"""
print()
# 省略
for i in range(10):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9

# ---------------------------------------------

"""
    枚举
    enumerate() 用于将一个可遍历的数据对象(如列列表、元组或字符串串)组合为一个索引序列，
    同时列出数据和数据下标，一般用在 for 循环当中
"""
print('-' * 30, 'enumerate')
list1 = ['a', 'b', 'c', 'd', 'e']

for i in enumerate(list1):
    print(i, end=' ')  # (0, 'a') (1, 'b') (2, 'c') (3, 'd') (4, 'e')
print()

# 设置开始下标 1
for index, char in enumerate(list1, start=1):
    print(f'下标是{index}, 对应的字符是{char}')
"""
    下标是1, 对应的字符是a
    下标是2, 对应的字符是b
    下标是3, 对应的字符是c
    下标是4, 对应的字符是d
    下标是5, 对应的字符是e
"""

# ---------------------------------------------

"""
    tuple()  将某个序列转换成元组
    list()  将某个序列转换成列表
    set()  将某个序列转换成集合
"""
print('-' * 30, 'tuple')

list1 = [10, 20, 30, 40, 50, 20]
s1 = {100, 200, 300, 400, 500}
print(tuple(list1))  # (10, 20, 30, 40, 50, 20)
print(tuple(s1))  # (100, 200, 300, 400, 500)

# ---------------------------------------------

