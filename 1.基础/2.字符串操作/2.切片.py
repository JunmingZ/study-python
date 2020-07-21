"""
    切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作。
    序列[开始位置下标:结束位置下标:步长]
"""

"""
    abcdefg
    0123456     正数
    7654321     负数
"""
name = "abcdefg"
print(name[2:5:1])  # cde   结束位置下标都不读取 和for循环所遇到的range函数一样
print(name[2:5])  # cde     默认步长是1
print(name[:5])  # abcde    结束位置下标都不读取 和for循环所遇到的range函数一样
print(name[1:])  # bcdefg   初始位置不同于结束位置，初始位置读取
print(name[:])  # abcdefg
print(name[::2])  # aceg
print(name[:-1])  # abcdef  负1表示倒数第一个数据，相当于从最后1开始数起,注意起始不是0
print(name[-7:])  # abcdefg
print(name[-4:-1])  # def
print(name[::-1])  # gfedcba    颠倒，字符串反转
