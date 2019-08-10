import Temperature, Speed

c = Temperature.Celcius()
k = Temperature.Kelvin()
f = Temperature.Fahrenheit()

km = Speed.Kilometers()
mp = Speed.Miles()
m = Speed.Meters()

print("Welcome to the unit converter!")

while True:

    print("You have following units to choose: \nTemperature: Kelvin, Celcius, Fahrenheit \nVelocity: km/h, m/s, mph")
    print("Choose the first unit which you want to convert: ")
    pierwsza_jednostka = input()
    pierwsza_jednostka = pierwsza_jednostka.lower()

    print("Choose the second unit which you want to convert: ")
    druga_jednostka = input()
    druga_jednostka = druga_jednostka.lower()

    if pierwsza_jednostka == "celcjusz" and druga_jednostka == "kelvin":
        c.celcius_to_kelvin()
        break

    elif pierwsza_jednostka == "celcjusz" and druga_jednostka == "fahrenheit":
        c.celcius_to_fahrenheit()
        break

    elif pierwsza_jednostka == "kelvin" and druga_jednostka == "celcjusz":
        k.kelvin_to_celcius()
        break

    elif pierwsza_jednostka == "kelvin" and druga_jednostka == "fahrenheit":
        k.kelvin_to_fahrenheit()
        break

    elif pierwsza_jednostka == "fahrenheit" and druga_jednostka == "celcjusz":
        f.fahrenheit_to_celcius()
        break

    elif pierwsza_jednostka == "fahrenheit" and druga_jednostka == "kelvin":
        f.fahrenheit_to_kelvin()
        break

    elif pierwsza_jednostka == "km/h"  and druga_jednostka == "mph":
        km.kilometers_to_miles()
        break

    elif pierwsza_jednostka == "km/h" and druga_jednostka == "m/s":
        km.kilometers_to_meters()
        break

    elif pierwsza_jednostka == "m/s" and druga_jednostka == "km/h":
        m.meters_to_kilometers()
        break

    elif pierwsza_jednostka == "m/s" and druga_jednostka == "mph":
        m.meters_to_miles()
        break

    elif pierwsza_jednostka == "mph" and druga_jednostka == "km/h":
        mp.miles_to_kilometers()
        break

    elif pierwsza_jednostka == "mph" and druga_jednostka == "m/s":
        mp.miles_to_meters()
        break

    else:
        print("Unknown unit.")

f = input("Press enter to leave.")


