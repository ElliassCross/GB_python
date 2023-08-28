N = int(input('Введите количество монет '))
heads = tails = 0
for i in range(N):
    x = int(input('Орел(1) или решка(0)? '))
    if x == 1:
        heads += 1
    else:
        tails += 1
if heads < tails:
    print(f'Переверните {heads} монет с орла на решку, их меньше всего')
elif heads == tails:
    print(f'Количество орлов и решек одинаково, по {heads} штук')
else:
    print((f'Переверните {tails} монет с решки на орла, их меньше всего'))