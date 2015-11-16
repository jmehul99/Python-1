def display():
    min = int(input("Enter the starting number : "))
    max = int(input("Enter the ending number :"))
    for i in range(min,max+1):
        if(i % 2 != 0):
            print(i)
if __name__ == '__main__':
    display()
