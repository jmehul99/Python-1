def main():
    a = int(input("Enter any number : "))
    print("Factorial value = %d"%fact(a))
def fact(x):
    if(x==1 or x == 0):
        return 1
    else:
        return(x*fact(x-1))


if __name__ == '__main__':
    main()
