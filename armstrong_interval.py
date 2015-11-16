def armstrong():
    min = int(input("Enter the starting number : "))
    max = int(input("Enter the ending number : "))
    for num in range(min,max):
        l = 0
        temp = num
        while(num > 0):
            z = num % 10
            num = int(num/10)
            l=l+z**3
        if(temp == l):
            print(l)
if __name__ == '__main__':
    armstrong()
