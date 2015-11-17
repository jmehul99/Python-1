def hcf():
    print("Enter two integers : ")
    a = int(input())
    b = int(input())
    while(b != 0):
        t = b
        b = a % b
        a = t
    gcd = a
    print("GCD is %d"%gcd)
if __name__ == '__main__':
    hcf()
