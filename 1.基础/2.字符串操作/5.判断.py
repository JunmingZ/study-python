"""
    startswith()    检查字符串是否是以指定子串开头
    endswith()      检查字符串是否是以指定子串结尾
    isalpha()       检查字符串至少有一个字符并且所有字符都是字母
    isdigit()       检查字符串只包含数字
    isalnum()       检查字符串至少有一个字符并且所有字符都是字母或数字
    isspace()       检查是否只有空格
"""

"""
    startswith()：检查字符串是否是以指定子串开头，是则返回 True，否则返回 False。如果设置开始和结束位置下标，则在指定范围内检查。
    字符串序列.startswith(⼦串, 开始位置下标, 结束位置下标) 
"""
print('-' * 30, 'startswith()')


mystr = "hello world"
print(mystr.startswith('hello'))    # True
print(mystr.startswith('hello', 5, 20))     # False

# --------------------------------------------------------

"""
    endswith()：检查字符串是否是以指定子串结尾，是则返回 True，否则返回 False。如果设置开始和结束位置下标，则在指定范围内检查。
    字符串序列.endswith(子串, 开始位置下标, 结束位置下标) 
"""
print('-' * 30, 'endswith()')


mystr = "hello world"
print(mystr.endswith('ld'))     # True
print(mystr.endswith('ldL'))    # False
print(mystr.endswith('ld', 2, 5))    # False

# --------------------------------------------------------

"""
    isalpha()：如果字符串至少有一个字符并且所有字符都是字⺟则返回 True, 否则返回 False。 
"""
print('-' * 30, 'isalpha()')

mystr1 = 'hello'
mystr2 = 'hello0'
mystr3 = ' '
mystr4 = 'a'
print(mystr1.isalpha())  # True
print(mystr2.isalpha())  # False
print(mystr3.isalpha())  # False
print(mystr4.isalpha())  # True

# --------------------------------------------------------

"""
    isdigit()：如果字符串只包含数字则返回 True 否则返回 False。
"""
print('-' * 30, 'isdigit()')

mystr1 = 'aaa12345'
mystr2 = '12345'

print(mystr1.isdigit())  # False
print(mystr2.isdigit())  # True

# --------------------------------------------------------

"""
    isalnum()：如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回False。
"""
print('-' * 30, 'isalnum()')

mystr1 = 'aaa12345'
mystr2 = '12345-'
mystr3 = 'a'
mystr4 = '2'

print(mystr1.isalnum())     # True
print(mystr2.isalnum())     # False
print(mystr3.isalnum())     # True
print(mystr4.isalnum())     # True


# --------------------------------------------------------

"""
    isspace()：如果字符串中只包含空白，则返回 True，否则返回 False。
"""
print('-' * 30, 'isspace()')

mystr1 = '1 2 3 4 5'
mystr2 = ' '

print(mystr1.isspace())     # False
print(mystr2.isspace())     # True
