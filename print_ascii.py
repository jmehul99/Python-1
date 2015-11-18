def ascii1():
    for i in range(256):
        x = str(i)
        y = chr(i)
        print("ASCII value of %c is %s"%(y,x))
if __name__ == '__main__':
    ascii1()
