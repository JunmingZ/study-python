"""
    与： and   x and y  如果 x 为 False，x and y 返回 False，否则它返回 y 的值。
    或：or    x or y   如果 x 是 True，它返回 True，否则它返回 y 的值。
    非：not
"""

# 非0为真(True)  0 代表 False
a = 0
b = 5
c = 10
# and运算符，只要有一个值为0，则结果为0，否则结果为最后一个非0数字
# 第一个是False, 后面不再执行
print(a and b)  # 0
print(b and a)  # 0
print(a and c)  # 0
print(c and a)  # 0
print(b and c)  # 10
print(c and b)  # 5

print('-' * 20)
# or运算符，只有所有值为0结果才为0，否则结果为第一个非0数字
# 第一个是True，后面不再执行
print(a or b)  # 5
print(a or c)  # 10
print(b or c)  # 5
