def table():
    num = int(input("Enter the multiplicand number : "))
    end = int(input("Enter the end multiplier number : "))
    for i in range(1,end+1):
        print("%d x %d = %d"%(i,num,num*i))
if __name__ == '__main__':
    table()
