a=0
b=1
sum=0
n=int(input('enter the value'))
if n<=0:
    print("enter num greater than 0")
else:
    for i in range(0,n):
        print("",sum)
        a=b
        b=sum
        sum=a+b
    
