def main():
    year = int(input("Enter a year to check if it is a leap year: "))
    if(year  % 400 == 0):
        print("%d is a leap year"% year)
    elif(year % 100 == 0):
        print("%d is not a leap year"% year)
    elif(year % 4 == 0):
        print("%d is a leap year"% year)
    else:
        print("%d is not a leap year"% year)
if __name__ == '__main__':
    main()
