class Kilometers():

    def kilometers_to_miles(self):
        print("Insert the value of velocity in km/h which you want convert to mph:")
        kilometers_ktmp = float(input())
        if kilometers_ktmp <= 0:
            print("Unknown value of velocity!")
        else:
            miles_ktm = kilometers_ktmp / 1.609344
            print("Result is {} mph.".format(miles_ktm))

    def kilometers_to_meters(self):
        print("Insert the value of velocity in km/h which you want convert to m/s:")
        kilometers_ktm = float(input())
        if kilometers_ktm <= 0:
            print("Unknown value of velocity!")
        else:
            meters_ktm = kilometers_ktm / 3.6
            print("Result is {} m/s.".format(meters_ktm))

class Meters():

    def meters_to_kilometers(self):
        print("Insert the value of velocity in m/s which you want convert to km/h:")
        meters_mtk = float(input())
        if meters_mtk <= 0:
            print("Unknown value of velocity!")
        else:
            kilometers_mtk = meters_mtk * 3.6
            print("Result is {} km/h.".format(kilometers_mtk))

    def meters_to_miles(self):
        print("Insert the value of velocity in km/h which you want convert to mph:")
        meters_mtm = float(input())
        if meters_mtm <= 0:
            print("Unknown value of velocity!")
        else:
            miles_mtm = meters_mtm * 2.23693629
            print("Result is {} mph.".format(miles_mtm))

class Miles():

    def miles_to_kilometers(self):
        print("Insert the value of velocity in mph which you want convert to km/h:")
        miles_mtk = float(input())
        if miles_mtk <= 0:
            print("Unknown value of velocity!")
        else:
            kilometers_mptk = miles_mtk * 1.609344
            print("Result is {} km/h.".format(kilometers_mptk))

    def miles_to_meters(self):
        print("Insert the value of velocity in mph which you want convert to m/s:")
        miles_mptk = float(input())
        if miles_mptk <= 0:
            print("Unknown value of velocity!")
        else:
            meters_mptk = miles_mptk / 2.23693629
            print("Result is {} m/s.".format(meters_mptk))

