name= input("Enter your name: ")
print("hello", name)
age= input("Enter your age: ")

try:
    age = int(age)
    print("you were born in", 2025-age)
except:
    print("i am sorry", name, "but that is not a real number")
else:
    print("thank you for playing", name, "youre the ultimate GOAT")