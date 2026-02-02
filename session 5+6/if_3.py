# case 3: multiple choices

import random
a = random.randint(1, 10)
b = random.randint(1, 10)
print("a is", a)
print("b is", b)

if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is not greater than b")
    
