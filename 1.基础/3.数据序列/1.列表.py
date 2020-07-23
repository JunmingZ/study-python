"""
    查找
    index()：返回指定数据所在位置的下标 。
    列表序列.index(数据, 开始位置下标, 结束位置下标)
    找不到会报错
"""
print('-' * 20, 'index')
name_list = ['Tom', 'Lily', 'Rose']
print(name_list.index('Lily', 0, 2))  # 1
print(name_list.index('Lily'))  # 1

try:
    print(name_list.index('hehehhe'))
except Exception as result:
    print(result)   # 'hehehhe' is not in list

# --------------------------------------------------
"""
    count()：统计指定数据在当前列表中出现的次数。
"""
print('-' * 20, 'count')
name_list = ['Tom', 'Lily', 'Rose']
print(name_list.count('Lily'))  # 1

# --------------------------------------------------


"""
    len()：访问列表长度，即列表中数据的个数。
"""
print('-' * 20, 'len')
name_list = ['Tom', 'Lily', 'Rose']
print(len(name_list))  # 3

# --------------------------------------------------


"""
    in：判断指定数据在某个列表序列，如果在返回True，否则返回False
"""
print('-' * 20, 'in')

name_list = ['Tom', 'Lily', 'Rose']
print('Lily' in name_list)  # True
print('Lilys' in name_list)  # False

# --------------------------------------------------


# 尝试对字符串使用
str = 'hello world'
print('o' in str)  # True

# --------------------------------------------------


"""
    not in：判断指定数据不在某个列表序列，如果不在返回True，否则返回False
"""
print('-' * 20, 'not in')
name_list = ['Tom', 'Lily', 'Rose']
print('Lily' not in name_list)  # False
print('Lilys' not in name_list)  # True

# --------------------------------------------------


"""
    在结尾追加单个元素
    列表序列.append(数据) 
"""
print('-' * 20, 'append')

name_list = ['Tom', 'Lily', 'Rose']
name_list.append('xiaoming')
print(name_list)  # ['Tom', 'Lily', 'Rose', 'xiaoming']

# --------------------------------------------------


"""
    extend()：列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表
"""

print('-' * 20, 'extend')
name_list = ['Tom', 'Lily', 'Rose']
name_list.extend('xiaoming')
print(name_list)  # ['Tom', 'Lily', 'Rose', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g']

# --------------------------------------------------
# 尝试元组 集合
name_list = ['Tom', 'Lily', 'Rose']
name_list.extend(('a', 'b'))
name_list.extend({'name': 'hong', 'age': 10})
print(name_list)  # ['Tom', 'Lily', 'Rose', 'a', 'b', 'name', 'age']
# 字典的value不在扩展范围中


# --------------------------------------------------


"""
    insert()：指定位置新增数据。
    列表序列.insert(位置下标, 数据) 
"""
print('-' * 20, 'insert')
name_list = ['Tom', 'Lily', 'Rose']
name_list.insert(1, 'xiaoming')
print(name_list)  # ['Tom', 'xiaoming', 'Lily', 'Rose']

# --------------------------------------------------


"""
    删除
    del 目标 
"""
print('-' * 20, 'del')

name_list = ['Tom', 'Lily', 'Rose']
# 结果：报错提示：name 'name_list' is not defined
del name_list
try:
    print(name_list)
except Exception as result:
    print(result)  # name 'name_list' is not defined

# 删除指定内容
name_list = ['Tom', 'Lily', 'Rose']
del name_list[0]
print(name_list)  # ['Lily', 'Rose']

# 尝试字符串
str = 'hello world'
try:
    del str[3]
    print(str)
except Exception as result:
    print(result)  # 'str' object doesn't support item deletion

# --------------------------------------------------

"""
    pop()：删除指定下标的数据(默认为最后一个)，并返回该数据。
    列表序列.pop(下标)
"""

print('-' * 20, 'pop')
name_list = ['Tom', 'Lily', 'Rose']
del_name = name_list.pop(1)
print(del_name)  # Lily  返回删除的数据
print(name_list)  # ['Tom', 'Rose']

# --------------------------------------------------


"""
    remove()：移除列表中某个数据的第一个匹配项
    列表序列.remove(数据)
"""
print('-' * 20, 'remove')
name_list = ['Tom', 'Lily', 'Rose']
name_list.remove('Rose')
print(name_list)  # ['Tom', 'Lily']

# --------------------------------------------------


"""
    清空
"""
print('-' * 20, 'clear')
name_list = ['Tom', 'Lily', 'Rose']
name_list.clear()
print(name_list)  # []

# --------------------------------------------------


"""
    逆置：reverse()
"""

print('-' * 20, 'reverse')
num_list = [1, 5, 2, 3, 6, 8]
num_list.reverse()
print(num_list)  # [8, 6, 3, 2, 5, 1]

# 使用切片逆置
print(num_list[::-1])  # [1, 5, 2, 3, 6, 8]

# --------------------------------------------------
"""
    排序：sort()
    列表序列.sort( key=None, reverse=False) 
    reverse = True 降序， reverse = False 升序（默认）
"""
print('-' * 20, 'sort')
num_list = [1, 5, 2, 3, 6, 8]
num_list.sort()
print(num_list)  # [1, 2, 3, 5, 6, 8]

# --------------------------------------------------


"""
    复制 copy()
"""
print('-' * 20, 'copy')
name_list = ['Tom', 'Lily', 'Rose']
name_li2 = name_list.copy()
print(name_li2)  # ['Tom', 'Lily', 'Rose']
name_li2[1] = 'hehe'
print(name_list)  # ['Tom', 'Lily', 'Rose'] 不会因为拷贝元素的改变而改变

# 尝试多内容拷贝
name_list = ['Tom', 'Lily', 'Rose', ['a', 'b'], ('a', 'b'), {'name': 'a', 'age': 10}]
name_li2 = name_list.copy()
print(name_li2)  # ['Tom', 'Lily', 'Rose', ['a', 'b'], ('a', 'b'), {'name': 'a', 'age': 10}]
