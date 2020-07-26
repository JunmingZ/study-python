"""
    文件对象.read(num)
    num表示要从文件中读取的数据的长度（单位是字节）,无则是读取全部
    直接读取
"""

f = open('1.txt', 'r')

temp = f.read()

print(temp)

"""
    abcdefg
    hijklmn
    opqrstu
    vwxyz
"""

# -------------------------------------------------------------

print('-' * 30, 'readlines')


"""
    seek() 方法用于移动文件读取指针到指定位置。
    fileObject.seek(offset[, whence])
    offset -- 开始的偏移量，也就是代表需要移动偏移的字节数，如果是负数表示从倒数第几位开始。
    whence -- 可选，默认值为 0。 给 offset 定义一个参数，表示要从哪个位置开始偏移
            0 代表从文件开头开始算起，
            1 代表从当前位置开始算起，
            2 代表从文件末尾算起。
"""

# 重新设置文件读取指针到开头
f.seek(0, 0)


"""
    readlines()
    返回的是一个列表，其中每一行的数据为一个元素
"""

content = f.readlines()
print(content)  # ['abcdefg\n', 'hijklmn\n', 'opqrstu\n', 'vwxyz']

# -------------------------------------------------------------

print('-' * 30, 'readline')
f.seek(0, 0)
"""
    readline() 一次读取一行内容。
    在读取时会有指针记录读取的位置
"""

content = f.readline()
print(f'第一行：{content}')  # 第一行：abcdefg
content = f.readline()
print(f'第二行：{content}')  # 第二行：hijklmn


f.close()

