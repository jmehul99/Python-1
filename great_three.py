print('Enter the numbers')
a=int(input())
b=int(input())
c=int(input())
if(a>b):
    if(a>c):
        print(a,"is largest number")
    else:
        print(c,"is Largest number")
elif(b>c):
    print(b,"is Largest number")
else:
    print(c,"is Largest number")
