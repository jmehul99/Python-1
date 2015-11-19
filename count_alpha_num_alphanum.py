def main():
  string = str(input("Enter the string"))
  alpha = 0
  spl = 0
  num = 0
  max = len(string)
  l = list(string)
  for i in range(0,max):
    a = str(l[i])
    if(a.isalpha() == True):
        alpha += 1
    elif(a.isdigit() == True):
        num += 1
    else:
        spl += 1
  print("alpha = %d num = %d special =%d"%(alpha,num,spl))

if __name__ == '__main__':
    main()
