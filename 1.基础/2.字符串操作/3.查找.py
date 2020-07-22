"""
    find()：检测某个子串是否包含在这个字符串中，如果在,返回这个子串开始的位置下标，否则则返回-1
    字符串序列.find(子串, 开始位置下标, 结束位置下标)
"""
print('-' * 30, 'find')
# --------------------------------------------------------
mystr = "检测某个子串是否包含在这个字符串中，如果在,返回这个子串开始的位置下标，否则则返回-1"
print(mystr.find('个子'))  # 3
print(mystr.find('个子', 15, 30))  # 25
print(mystr.find('急急如意令'))  # -1

print('-' * 30, 'index')
# --------------------------------------------------------

"""
    index()：检测某个子串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则报异常。
    字符串序列.index(子串, 开始位置下标, 结束位置下标) 
"""

mystr = "检测某个子串是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则报异常"
print(mystr.index('个'))  # 3
print(mystr.index('个', 15, 30))  # 24
try:
    print(mystr.index('个个'))  # 报错
except Exception as result:
    print(result)  # substring not found 意为 子串没找到

# --------------------------------------------------------
print('-' * 30, 'rfind')

"""
    rfind()： 和find()功能相同，但查找方向为右侧开始。
    rindex()：和index()功能相同，但查找方向为右侧开始。
    count()：返回某个子串在字符串中出现的次数
"""

mystr = "rfind()： 和find()功能相同，但查找方向为右侧开始。"
print(mystr.rfind('开始'))  # 29
print(mystr.rfind('开始吧'))  # -1

# --------------------------------------------------------
print('-' * 30, 'rindex')

mystr = "rindex()：和index()功能相同，但查找方向为右侧开始。"
print(mystr.rindex('开始'))  # 30
try:
    print(mystr.rindex('开始吧'))  # -1
except Exception as result:
    print(result)  # substring not found 意为 子串没找到

# --------------------------------------------------------
print('-' * 30, 'count')

"""
    字符串串序列列.count(⼦子串串, 开始位置下标, 结束位置下标)
"""

mystr = "hello world, I am studying Python. How about you. I would kill you"
print(mystr.count('I'))  # 2
print(mystr.count('amdfa'))  # 0
print(mystr.count('I', 0, 20))  # 1
