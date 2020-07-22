"""
    字符串属于不可变类型，所以修改操作本质重新开辟空间保存修改的值
    replace()       替换
    split()         分割
    join()          合并
    capitalize()    转换第一个字符成大写
    title()         将字符串每个单词首字母转换成大写
    lower()         将字符串中大写转小写。
    upper()         将字符中小写转大写。
    lstrip()        删除字符串左侧空白字符。
    rstrip()        删除字符串右侧空白字符。
    strip()         删除字符串两侧空白字符
    ljust()         返回一个原字符串左对齐,并使用指定字符(默认空格)填充至对应长度 的新字符串。
    rjust()         和 ljust()相反
    center()        返回一个原字符串居中对齐,并使用指定字符(默认空格)填充至对应长度的新字符串，语法和ljust()相同。
"""

"""
    字符串序列.replace(旧子串, 新子串, 替换次数) 
"""
print('-' * 30, 'replace()')

mystr = "字符串序列.replace(旧子串, 新子串, 替换次数)"
print(mystr.replace('串', '咧咧咧'))  # 字符咧咧咧序列.replace(旧子咧咧咧, 新子咧咧咧, 替换次数)  默认全替换
print(mystr.replace('串', '咧咧咧', 2))  # 字符咧咧咧序列.replace(旧子咧咧咧, 新子串, 替换次数)
print(mystr)  # 字符串序列.replace(旧子串, 新子串, 替换次数)

# ------------------------------------------------------------

"""
   字符串序列.split(分割字符, num)
   num表示的是分割字符出现的次数，即将来返回数据个数为num+1个。 如 2 返回列表长度为3
   返回一个列表
"""
print('-' * 30, 'split()')

mystr = "字符串序列.split(分割字符, num)，字符串，字符串，字符串，字符串，字符串，"
print(mystr.split('，'))  # ['字符串序列.split(分割字符, num)', '字符串', '字符串', '字符串', '字符串', '字符串', '']
print(mystr.split('，', 2))  # ['字符串序列.split(分割字符, num)', '字符串', '字符串，字符串，字符串，字符串，']
print(len(mystr.split('，', 2)))  # 3


# ------------------------------------------------------------

"""
   字符或子串.join(多字符串组成的序列)
   用一个字符或子串合并字符串，即是将多个字符串合并为一个新的字符串
"""
print('-' * 30, 'join()')

list1 = ['你', '好', '吗', '啊']
t1 = ('aa', 'b', 'cc', 'ddd')  # 元组
print(' '.join(list1))  # 你 好 吗 啊
print('...'.join(t1))   # aa...b...cc...ddd

# ------------------------------------------------------------

"""
    转换第一个字符成大写
"""
print('-' * 30, 'capitalize()')

mystr = "hello world"
print(mystr.capitalize())

# ------------------------------------------------------------

"""
    title()：将字符串每个单词首字母转换成大写
"""
print('-' * 30, 'title()')

mystr = "hello world he he,he he.he(wo)"
print(mystr.title())  # Hello World He He,He He.He(Wo)


# ------------------------------------------------------------

"""
    lower()：将字符串中大写转小写。
"""
print('-' * 30, 'lower()')

mystr = "hello world HELLO WORLD"
print(mystr.lower())  # hello world hello world

# ------------------------------------------------------------

"""
    upper()：将字符串中小写转大写。
"""
print('-' * 30, 'upper()')

mystr = "hello world"
print(mystr.upper())  # HELLO WORLD

# ------------------------------------------------------------

"""
    lstrip()：删除字符串左侧空白字符。
"""
print('-' * 30, 'lstrip()')

mystr = "      hello world     "
print(mystr.lstrip())  # hello world      右侧空格还存在


# ------------------------------------------------------------


"""
    rstrip()：删除字符串右侧空白字符。
"""
print('-' * 30, 'rstrip()')

mystr = "      hello world     "
print(mystr.rstrip())  #       hello world  左侧空格还存在

# ------------------------------------------------------------

"""
    strip()：删除字符串两侧空白字符
"""
print('-' * 30, 'strip()')

mystr = "      hello world     "
print(mystr.strip())  # hello world

# ------------------------------------------------------------


"""
    ljust()：返回一个原字符串左对齐,并使用指定字符(默认空格)填充至对应长度 的新字符串。
    字符串序列.ljust(长度, 填充字符) 
    注意：字符串序列的长度在包含在这个长度
"""
print('-' * 30, 'ljust()')

mystr = "hello"
print(mystr.ljust(10, '.'))  # hello world

# ------------------------------------------------------------

"""
    center()：返回一个原字符串居中对齐,并使用指定字符(默认空格)填充至对应长度的新字符串，语法和ljust()相同。
"""

print('-' * 30, 'center()')

mystr = "hello"
print(mystr.center(11, '.'))  # ...hello...
