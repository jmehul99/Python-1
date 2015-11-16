def main():
    n = int(input('Enter the limit : '))
    x = 0
    while(n > 0):
        x += n
        n -= 1
    print(x)
if __name__ == '__main__':
    main()
