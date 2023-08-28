x = int(input('Первое натуральное число: '))
y = int(input('Второе натуральное число: '))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)