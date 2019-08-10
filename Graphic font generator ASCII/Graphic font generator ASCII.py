import pyfiglet, Czcionka

cz = Czcionka


welcome = pyfiglet.figlet_format("Welcome to ASCII font generator!")
print(welcome)
cz.czcionka()

while True:
    print("Please choose a number of font:")
    x = input()

    if not x.isdigit():
        print("Not a number! Insert a correct number!")

    elif x == "1":
        font = "default_font"
        break

    elif x == "2":
        font = "slant"
        break

    elif x == "3":
        font = "3-d"
        break

    elif x == "4":
        font = "3x5"
        break

    elif x == "5":
        font = "5lineoblique"
        break

    elif x == "6":
        font = "alphabet"
        break

    elif x == "7":
        font = "banner3-D"
        break

    elif x == "8":
        font = "doh"
        break

    elif x == "9":
        font = "isometric1"
        break

    elif x == "10":
        font = "letters"
        break

    elif x == "11":
        font = "alligator"
        break

    elif x == "12":
        font = "dotmatrix"
        break

    elif x == "13":
        font = "bubble"
        break

    elif x == "14":
        font = "bulbhead"
        break

    elif x == "15":
        font = "digital"
        break

    else:
        print("Not a correct number! Insert a correct number!")

print("Insert a sentence which you want to generate.")
sentence = input()
pyfiglet.print_figlet(sentence, font= font)
