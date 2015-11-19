def words():
    string = str(input("Enter a string : "))
    l = string.split()
    length = len(l)
    print("Number of words : %d"%length)

if __name__ == '__main__':
    words()
