def fact():
    num = int(input("Enter a number : "))
    fact = 1
    while(num>0):
        fact = fact*num
        num -=1
    print("The factorial of given number %d"%fact)
if __name__ == '__main__':
    fact()
