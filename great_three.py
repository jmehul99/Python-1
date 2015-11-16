def main():
    print('Enter three numbers : ')
    a = int(input())
    b = int(input())
    c = int(input())
    if(a > b):
        if(a > c):
            print(a,"is largest number")
        else:
            print(c,"is Largest number")
    elif(b > c):
        print(b,"is Largest number")
    else:
        print(c,"is Largest number")
if __name__ == '__main__':
    main()
