def Leap_year_checker(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("The year is leap year")
            else:
                print("The year is not a leap year")
        else:
            print("The Year is a leap year")
    else:
        print("The year is not a leap year")



if __name__ == '__main__':
    year = int(input('Enter year that you want to check whether it is leap year or not: '))
    Leap_year_checker(year)