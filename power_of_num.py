def power():
    number = int(input("Enter a number:"))
    power = int(input("Enter the power value: "))
    answer = number
    for x in range(1,power):
        answer *= number
    print(answer)
if __name__ == '__main__':
    power()
