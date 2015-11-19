def main():
  string = str(input("Enter the string"))
  alpha = 0
  alnum = 0
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
        alnum += 1
  print("alpha = %d num = %d alphanum =%d"%(alpha,num,alnum))

if __name__ == '__main__':
    main()
