def swap():
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    temp = a
    a = b
    b = temp
    print(a,b)
if __name__ == '__main__':
    swap()
