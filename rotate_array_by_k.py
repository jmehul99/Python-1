def main():
    n = int(input("Enter the number of elements :"))
    array = []
    new_array = []
    print("Enter the elements of array :")
    for i in range(n):
        array.append(int(input()))
    k = int(input("Enter No. of rotations : "))
    for i in range(k):
        new_array.append(array[n-1])
        for j in range(n-1):
            new_array.append(array[j])
        for j in range(n):
            array[j] = new_array[j]
        new_array.clear()
    print(array)

if __name__ == '__main__':
    main()
