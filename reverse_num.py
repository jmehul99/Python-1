def reverse():
    num = int(input("Enter a number : "))
    ans = 0
    while(num > 0):
        a = num%10
        num = int(num/10)
        ans = ans*10+a
    print(ans)
if __name__ == '__main__':
    reverse()
