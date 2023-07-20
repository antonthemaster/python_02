import random


x = random.randint(4, 1024)
res = 1
powered_num = 2
print(x, '\n')
while powered_num < x:
    powered_num += powered_num
    print (res)
    res += 1
print('\n', pow(2, res - 1))

