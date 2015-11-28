def main():
    num = int(input("Enter the number : "))
    k = x = num
    temp = []
    while(k != 1):
        sum = 0
        new_array = split(k)
        for i in range(len(new_array)):
            sum += new_array[i]**2
        if(sum not in temp):
            temp.append(sum)
            k = sum
        else:
            print("%d is not a Happy Number"%num)
            break
    if(k == 1):
        print("%d is a Happy Number" % num)

def split(x):
    new_array = []
    while(x>0):
        new_array.append(x%10)
        x = int(x/10)
    return new_array

if __name__ == '__main__':
    main()
