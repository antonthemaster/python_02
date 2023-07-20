import random


x = random.randint(1, 1000)
y = random.randint(1, 1000)

product = x * y
summ = x + y
print(summ, product)

for i in range(1,1000):
    for j in range(1, 1000):
        if i + j == summ and i * j == product:
            print('x =', i, 'y =', j)
            break
