"""
    使用场景： 一个函数有一个返回值，并且只有一句代码
    lambda 参数列表 ： 表达式
"""

# 无参，返回100
fn1 = lambda: 100
print(fn1)  # <function <lambda> at 0x000001EDBC370B80>
print(fn1())  # 100

# ————————————————————————————————————————————————
print('-' * 20, '有参')

# 有参
print((lambda a, b: a + b)(1, 2))


# ------------------------------------------------
print('-' * 20, '应用')


students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}
]

# 按name值升序排列
students.sort(key=lambda x: x['name'])
print(students)  # [{'name': 'Jack', 'age': 22}, {'name': 'ROSE', 'age': 19}, {'name': 'TOM', 'age': 20}]
# 按name值降序排列
students.sort(key=lambda x: x['name'], reverse=True)
print(students)  # [{'name': 'TOM', 'age': 20}, {'name': 'ROSE', 'age': 19}, {'name': 'Jack', 'age': 22}]
# 按age值升序排列
students.sort(key=lambda x: x['age'])
print(students)  # [{'name': 'ROSE', 'age': 19}, {'name': 'TOM', 'age': 20}, {'name': 'Jack', 'age': 22}]


