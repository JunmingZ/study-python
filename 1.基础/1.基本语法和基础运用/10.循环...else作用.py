"""
    else指的是循环正常结束之后要执行的代码
"""
i = 1
while i <= 5:
    if i == 3:
        print('执行continue')
        i += 1
        continue
    print(f'i的值为{i}')
    i += 1
else:
    print('执行else部分')

'''
    i的值为1
    i的值为2
    执行continue
    i的值为4
    i的值为5
    执行else部分
'''

print('-' * 30)
# ---------------------------------------

i = 1
while i <= 5:
    if i == 3:
        print('执行break')
        i += 1
        break
    print(f'i的值为{i}')
    i += 1
else:
    print('执行else部分')

'''
    i的值为1
    i的值为2
    执行break
'''