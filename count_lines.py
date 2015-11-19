def main():
    f = open("F:\example.txt") #path of example text file
    n =f.readlines()
    print("NO. of lines in the given text file : %d"%len(n))

if __name__ == '__main__':
    main()
