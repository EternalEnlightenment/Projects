print("Welcome to the Palindrome-match program.")

while True:
    print("Insert a word which you want to match:")
    slowo = input()
    slowo_odwrocone = slowo[::-1]

    if slowo.isdigit():
        print("{} is the digit, insert a word!".format(slowo))

    elif slowo == slowo_odwrocone:
        print("The word {} is the Palindrome.".format(slowo))
        break

    else:
        print("The word {} is the Palindrome.".format(slowo))
        break

exit = input("Press enter to exit.")
