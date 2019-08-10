import random

print("Welcome in guess the number game!\nThe program will generate a digit from 0 to 9.")

while True:

    print("Insert a digit from 0 to 9.")
    x = random.randint(0, 9)
    liczba = int(input())

    if x == liczba:
        print("You win!")

    else:
        print("You lose!")

    print("If you want to play again press enter, otherwise write: no")

    y = input()
    y = y.lower()

    if y == "no":
        break

print("To exit press enter")
