def main():
    ex = str(input("Enter the string : "))
    if(ex == 'q' or ex == 'Q'):
        quit
    else:
        main()

if __name__ == '__main__':
    main()
