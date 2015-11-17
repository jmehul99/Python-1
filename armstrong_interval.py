def armstrong():
    min = int(input("Enter the starting number : "))
    max = int(input("Enter the ending number : "))
    for num in range(min,max):
        l = 0
        temp = num
        temp2 = num
        count = 0
        while(temp2 > 0):
            temp2 = int(temp2 / 10)
            count += 1
        while(num > 0):
            z = num % 10
            num = int(num/10)
            l=l+z**count
        if(temp == l):
            print(l)
if __name__ == '__main__':
    armstrong()
