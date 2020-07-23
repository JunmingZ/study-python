"""
    无序，无下标，不重复，空集合只能用set()
    因为{} 会创建空字典
    不能添加字典,列表.
    可以添加元组
"""

# ------------------------------------------
"""
    add() 添加
"""

print('-' * 20, 'add()')
s1 = {10, 20}
s1.add(100)
s1.add(10)
s1.add('你好')
try:
    s1.add({'name': '法海'})
except Exception as result:
    print(result)  # unhashable type: 'dict'

try:
    s1.add([1, 2])
except Exception as r:
    print(r)  # unhashable type: 'list'

try:
    s1.add((1, 2))
except Exception as r:
    print(r)

print(s1)  # {(1, 2), 100, 10, '你好', 20}

# ------------------------------------------

"""
    update(), 追加的数据是序列。
    类似 list 的 extend
    传进去的参数要可迭代
"""
print('-' * 20, 'update')

s1 = {10, 20}
try:
    s1.update(100)
except Exception as r:
    print(r)  # 'int' object is not iterable
s1.update([100, 200])
s1.update('abc')
print(s1)  # {'a', 100, 200, 10, 'c', 20, 'b'}

# ------------------------------------------

"""
    remove()，删除集合中的指定数据，如果数据不存在则报错KeyError。
"""

print('-' * 20, 'remove')
s1 = {10, 20}
s1.remove(10)
print(s1)  # {20}

try:
    s1.remove(1000)
except Exception as r:
    print(r)  # 1000

# ------------------------------------------
"""
    discard()，删除集合中的指定数据，如果数据不存在也不会报错。
"""
print('-' * 20, 'discard')
s1 = {10, 20}
s1.discard(10)
print(s1)  # {20}
s1.discard(1000)
print(s1)  # {20}


# ------------------------------------------
"""
    pop()，随机删除集合中的某个数据，并返回这个数据。
"""
print('-' * 20, 'pop')
s1 = {10, 20, 30, 40, 50}
del_num = s1.pop()
print(del_num)  # 40
print(s1)  # {10, 50, 20, 30}


# ------------------------------------------
"""
    in：判断数据在集合序列
    not in：判断数据不在集合序列
"""

print('-' * 20, 'in  not in')

s1 = {10, 20, 30, 40, 50}
print(10 in s1)  # True
print(10 not in s1)  # False
