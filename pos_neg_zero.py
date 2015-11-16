def main():#define main function
    num = int(input("Enter a number"))#getting an integer value
    if(num>0):      #checking the number is positive
        print("The number is positive")
    elif(num<0):    #checking the number is negative
        print("The number is negative")
    else:           #checking the number is equal to zero
        print("The number is equal to zero")
if __name__ == '__main__':
    main()      #calling main function
