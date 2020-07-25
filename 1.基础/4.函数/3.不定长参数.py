"""
    也叫可变参数
    包裹位置参数： *args         ==> 将接收的到参数封装成一个元组
    包裹关键字参数： **kwargs
"""


def user_info(*args):
    print(args)


user_info('TOM')  # ('TOM',)
user_info('TOM', 18)  # ('TOM', 18)


# ——--------------------------------------------------

print('-' * 30, '包裹关键字')


def user_info(**kwargs):
    print(kwargs)


user_info(name='TOM', age=18, id=110)  # {'name': 'TOM', 'age': 18, 'id': 110}


"""
    无论是包裹位置传递还是包裹关键字传递，都是一个组包的过程。
"""