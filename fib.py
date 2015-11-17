def fib():
    num = int(input("Enter the number of elements to be in fibonacci series : "))
    temp = 0
    temp1 = 1
    for i in range(0,num):
        ans = temp + temp1
        temp = temp1
        temp1 = ans
        print(ans)
if __name__ == '__main__':
    fib()
