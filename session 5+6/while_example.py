num = 1
while num <= 10:
    print(num)
    num = num + 1

import random
money = 10000
counter = 1
while money > 0:
    print(money)
    expense = random.randint(1, 100)
    print("iteriation: ", counter, "expense: ", expense)
    counter = counter + 1
    money = money - expense

counter = 1
while true:
    while money > 0:
        break
print(money)
expense = random.randint(1, 100)
print("iteriation: ", counter, "expense: ", expense)
counter = counter + 1
money = money - expense