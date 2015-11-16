def armstrong():
    num = int(input("Enter the number : "))
    temp = num
    l=0
    while(num > 0):
        z = num % 10
        num = int(num/10)
        l=l+z**3
    if(temp == l):
        print("Armstrong Number")
    else:
        print("Not an armstrong number")
if __name__ == '__main__':
    armstrong()
