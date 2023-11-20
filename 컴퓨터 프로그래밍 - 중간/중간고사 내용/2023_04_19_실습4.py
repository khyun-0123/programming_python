import random
count = 0
dice1, dice2, dice3 = 0, 0, 0

while True :
    count += 1
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    if (dice1 == dice2) and (dice2== dice3) :
        break
print(dice1, dice2, dice3, count)