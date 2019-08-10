import time

print("Welcome in the program to counting, insert a first number:")
y = int(input())

print("Insert a second number:")
x = int(input())

if x == y:
    print("The numbers are equal!")

print(y)

if x > y:
    while x > y:
        y += 1
        time.sleep(1)
        print(y)

if x < y:
    while x < y:
        y -= 1
        time.sleep(1)
        print(y)

input("Press enter to exit!")
