def main():
    string = str(input("Enter the sring : "))
    count = 0
    l = list(string)
    length = len(l)
    for i in range(0,length):
        x = str(l[i])
        if(x.isnumeric() == True):
            count += 1
    print("No. of Numeric character : %d"%count)

if __name__ == '__main__':
    main()
