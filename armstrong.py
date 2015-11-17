def armstrong():
    num = int(input("Enter the number : "))
    temp = num
    temp2 = num
    l=0
    count = 0
    while(temp2 > 0):
        temp2 = int(temp2 / 10)
        count += 1
    while(num > 0):
        z = num % 10
        num = int(num/10)
        l=l+z**count
    if(temp == l):
        print("Armstrong Number")
    else:
        print("Not an armstrong number")
if __name__ == '__main__':
    armstrong()
