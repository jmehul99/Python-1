def main():
    string = str(input("Enter the string : "))
    new = []
    n =len(string)
    l = list(string)
    for i in range(0,n):
        a = str(l[i])
        if(a.isupper() == True):
            new.append(a.lower())
        else:
            new.append(a.capitalize())
    string = new[0]
    for i in range(0,n-1):
        string = string + new[i+1]
    print("The case swapped string is : %s"%string)

if __name__ == '__main__':
    main()
