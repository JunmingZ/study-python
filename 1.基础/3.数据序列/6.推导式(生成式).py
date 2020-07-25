"""
    列表推导式
"""

# 普通
list1 = [i for i in range(10)]
print(list1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 带if
list1 = [i for i in range(10) if i % 2 == 0]
print(list1)  # [0, 2, 4, 6, 8]

# 双层for
list1 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list1)  # [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# ------------------------------------------------------------

"""
    字典推导式
"""
print('-' * 30, '字典推导式')
# 合并列表为字典
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']
dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)  # {'name': 'Tom', 'age': 20, 'gender': 'man'}

# 提取字典中目标数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# 大于等于200的字典数据
count1 = {key: value for key, value in counts.items() if value >= 200}
print(count1)  # {'MBP': 268, 'DELL': 201}

# ------------------------------------------------------------

"""
    集合推导式
"""

print('-' * 30, '集合推导式')

list1 = [1, 1, 2]
set1 = {i ** 2 for i in list1}
print(set1)  # {1, 4}
