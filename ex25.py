def main():
    n = 0
    for i in range(0,16):
        n += i
    print("Sum of numbers 1 to 15 : %d"%n)
def odd():
    x = 0
    for i in range(15,46):
        if(i % 2 != 0):
            x += i
    print("Sum of odd numbers from 15 to 45 : %d"%x)
if __name__ == '__main__':
    main()
    odd()
