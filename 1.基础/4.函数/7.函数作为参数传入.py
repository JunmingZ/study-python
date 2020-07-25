from functools import reduce


def sum_num(a, b, f):
    return f(a) + f(b)


# abs 算绝对值
result = sum_num(-1, 2, abs)
print(result)  # 3

# ----------------------------------------------
"""
    内置高阶函数map 
    map(function, iterable, ...)
    第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
"""
print('-' * 20, 'map')
list1 = [1, 2, 3, 4, 5]

# ** 是指数运算 即x的平方
result = map(lambda x: x ** 2, list1)

print(list(result))  # [1, 4, 9, 16, 25]

# ----------------------------------------------

"""
    需要引入：from functools import reduce
    reduce(function, iterable[, initializer]) 
    iterable: 可迭代对象
    initializer -- 可选，初始参数
    
    会对参数序列中元素进行累积。
    reduce()传入的参数func必须接受2个参数
"""
print('-' * 20, 'reduce')

list1 = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, list1)

print(result)  # 15

# ----------------------------------------------

"""
    filter(function, iterable)
    iterable: 可迭代对象
    函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换
"""
print('-' * 20, 'filter')
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter(lambda x: x % 2 == 0, list1)
print(list(result))  # [2, 4, 6, 8, 10]
