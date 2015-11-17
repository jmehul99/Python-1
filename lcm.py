def lcm():
    print("Enter two integers : ")
    a = int(input())
    b = int(input())
    x = a
    y = b
    while(b != 0):
        t = b
        b = a % b
        a = t
    gcd = a
    lcm = (x*y)/gcd
    print("LCM is %d"%lcm)
if __name__ == '__main__':
    lcm()
