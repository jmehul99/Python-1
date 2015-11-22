def main():
    n = int(input("Enter the no. of elements :"))
    a = []
    print("Enter the array elemnts : ")
    for i in range(n):
        a.append(int(input()))
    new_array = []
    for i in range(n):
        num = a.count(a[i])
        new_array.append(num)
    for i in range(n):
        if(new_array[i] == 1):
            print("The number = %d"%a[i])


if __name__ == '__main__':
    main()
