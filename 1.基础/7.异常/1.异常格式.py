try:
    f = open('test.txt', 'r')
except Exception as result:
    f = open('test.txt', 'w')
    print(result)
else:  # 表示的是如果没有异常要执行的代码。
    print('没有异常，真开心')
finally:  # 表示的是无论是否异常都要执行的代码
    f.close()
    print('......')  # ......
