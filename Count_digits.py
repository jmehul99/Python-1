def main():
    n = int(input('Enter the integer : '))
    count = 0
    while(n > 0):
        n = int(n / 10)
        count += 1
    print(count)
if __name__ == '__main__':
    main()
