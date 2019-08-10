class Celcius():

    def celcius_to_kelvin(self):
        print("Insert the value of temperature in Celcius which you want convert to Kelvin:")
        celcius_ctk = float(input())
        if celcius_ctk < -273.15:
            print("Value of temperature is below zero absolute!")
        else:
            kelvin_ctk = celcius_ctk + 273.15
            print("Result is {} K.".format(kelvin_ctk))

    def celcius_to_fahrenheit(self):
        print("Insert the value of temperature in Celcius which you want convert to Fahrenheit:")
        celcius_ctf = float(input())
        if celcius_ctf < -273.15:
            print("Value of temperature is below zero absolute!")
        else:
            fahrenheit_ctf = celcius_ctf * (9 / 5) + 32
            print("Result is {} °F.".format(fahrenheit_ctf))

class Kelvin():

    def kelvin_to_celcius(self):
        print("Insert the value of temperature in Kelvin which you want convert to Celcius:")
        kelvin_ktc = float(input())
        if kelvin_ktc < 0:
            print("Value of temperature is below zero absolute!")
        else:
            celcius_ktc = kelvin_ktc - 273.15
            print("Result is {} °C.".format(celcius_ktc))

    def kelvin_to_fahrenheit(self):
        print("Insert the value of temperature in Kelvin which you want convert to Fahrenheit:")
        kelvin_ktf = float(input())
        if kelvin_ktf < 0:
            print("Value of temperature is below zero absolute!")
        else:
            fahrenheit_ktf = kelvin_ktf * (9 / 5) - 459.67
            print("Result is {} °F.".format(fahrenheit_ktf))

class Fahrenheit():

    def fahrenheit_to_celcius(self):
        print("WInsert the value of temperature in Fahrenheit which you want convert to Celcius:")
        fahrenheit_ftc = float(input())
        if fahrenheit_ftc < -459.67:
            print("Value of temperature is below zero absolute!")
        else:
            celcius_ftc = (fahrenheit_ftc - 32) * (5 / 9)
            print("Result is {} °C.".format(celcius_ftc))

    def fahrenheit_to_kelvin(self):
        print("Insert the value of temperature in Fahrenheit which you want convert to Klevin:")
        fahrenheit_ftk = float(input())
        if fahrenheit_ftk < -459.67:
            print("Value of temperature is below zero absolute!")
        else:
            kelvin_ftk = (fahrenheit_ftk + 459.67) * (5 / 9)
            print("Result is {} K.".format(kelvin_ftk))
