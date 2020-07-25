def return_num():
    return 100, 200


num1, num2 = return_num()
print(num1)  # 100
print(num2)  # 200


# ------------------------------------------------
print('-' * 30)


def return_dict():
    return {'name': 'admin', 'age': 10}


key1, key2 = return_dict()
print(key1)  # name
print(key2)  # age
