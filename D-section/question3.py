import random

number = set()

for i in range(1, 4):
    num = random.randint(1, 50)
    number.add(num)

print(f"\nThis is the main set : {number}")

number.add(60)

print(f"\nThis is the set after adding number : {number}\n")
