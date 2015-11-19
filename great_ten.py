def main():
    print("Enter the ten numbers : ")
    a =[]
    for i in range(10):
        a.append(int(input()))
    n = int(a[0])
    for i in range(10):
        if(a[i] > n):
            n = a[i]
    print("Greatest among ten numbers : %d"%n)

if __name__ == '__main__':
    main()
