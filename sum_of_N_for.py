def main():
    num = int(input("Enter a natural number"))
    count=0
    for x in range(0,num+1):
        count += x
    print(count)
if __name__ == '__main__':
    main()
