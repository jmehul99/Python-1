def main():
    num = int(input("Enter the number :"))
    i = 1
    while(i<num):
        i *= 2
    if(i == num and i != 1):
        print("It's power of 2")
    else:
        print("It's Not power of 2")

if __name__ == '__main__':
    main()
