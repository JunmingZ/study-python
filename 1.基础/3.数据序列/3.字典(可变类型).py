"""
    形似 JavaScript 的对象,但是不能像js一样直接引用，同样是脚本语言
"""

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}

# 尝试使用引用
try:
    print(dict1.name)
except Exception as result:
    print(result)  # 'dict' object has no attribute 'name'

# --------------------------------------------------------------

"""
    增加/修改： 存在则修改，不存在则增加
"""
print('-' * 30, '增加')

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict1['id'] = 1
print(dict1)  # {'name': 'Tom', 'age': 20, 'gender': '男', 'id': 1}

# --------------------------------------------------------------

"""
    删除
"""
print('-' * 30, '删除')
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
del dict1['gender']
print(dict1)  # {'name': 'Tom', 'age': 20}

# --------------------------------------------------------------

"""
    查 get()
    字典序列.get(key, 默认值) 
    找到返回第一个参数，没有返回第二个参数，默认None
"""
print('-' * 30, 'get()')

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.get('gender'))  # 男
print(dict1.get('hehehe'))  # None
print(dict1.get('hehehe', '抱歉不存在'))  # 抱歉不存在

# --------------------------------------------------------------

"""
    keys() 获取所有键
"""
print('-' * 30, 'keys()')
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(type(dict1.keys()), dict1.keys())  # <class 'dict_keys'> dict_keys(['name', 'age', 'gender'])

# 遍历获取值
for key in dict1.keys():
    print(f'key = {key}, value = {dict1[key]}')
"""
    key = name, value = Tom
    key = age, value = 20
    key = gender, value = 男
"""
# --------------------------------------------------------------

"""
   values() 获取所有值
"""
print('-' * 30, 'values()')

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.values())  # dict_values(['Tom', 20, '男'])

# --------------------------------------------------------------
"""
     items() 以元组形式组成的列表
"""
print('-' * 30, 'items()')

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.items())  # dict_items([('name', 'Tom'), ('age', 20), ('gender','男')])

# --------------------------------------------------------------
print('-' * 30, '尝试下标')

# 尝试下标
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
try:
    print(dict1[0])
except Exception as result:
    print(result)  # 0  报错
