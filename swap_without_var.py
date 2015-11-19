def swap():
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    a +=b
    b = a - b
    a = a - b
    print(a,b)
if __name__ == '__main__':
    swap()
