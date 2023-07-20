import random


coins_count = random.randint(5, 10)
print('total coins quantity: ', coins_count)
coins = list()
coins_to_flip = int()
for i_coin in range(coins_count):
    i_coin = random.randint(0, 1)
    if i_coin == 1:
        i_coin = 'head'
    else:
        i_coin = 'tail'
        coins_to_flip += 1
    coins.append(i_coin)
print(coins)
print('coins needs to flip: ', coins_to_flip)

