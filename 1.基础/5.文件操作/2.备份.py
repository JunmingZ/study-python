# 要备份文件名
filename = '1.txt'

# 组件备份文件名
# 先获取索引
index = filename.rfind('.')

# 通过切片抽取无后缀部分,并组装
newFileName = filename[:index] + '[备份]' + filename[index:]

# 以二进制形式读取
f = open(filename, 'rb')
w = open(newFileName, 'wb')

# 从f读取 写入到w
while True:
    con = f.read(1024)
    if len(con) == 0:
        break
    # 写入
    w.write(con)

# 关闭文件
f.close()
w.close()
