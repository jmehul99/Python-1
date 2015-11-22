def main():
    string = str(input("Enter the string : "))
    n =len(string)
    if(n%2 != 0):
        n = n-1
    l = list(string)
    a = 0
    while(a<n):
        temp = l[a]
        l[a] = l[a+1]
        l[a+1] = temp
        a = a+2
    ans = l[0]
    length = len(l)
    for i in range(0,length-1):
        ans = ans+l[i+1]
    print(ans)

if __name__ == '__main__':
    main()
