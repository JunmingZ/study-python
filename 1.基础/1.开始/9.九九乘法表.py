j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i}*{j}={j * i}', end='\t')
        i += 1
    print()
    j += 1

print('-' * 20)

# -----------------------------------

"""
    range(1, 10) 相当于 1 <= i < 10 的范围
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}*{i}={i * j}', end='\t')
    print()
