# print("hello world!")


n=int(input("enter a number: "))
while n!=1 and n!=4:
    total=0 
    while n>0:
        digit=n%10
        total=total+digit**2
        n=n//10
    n=total
if n==1:
    print("happy no")
else:
    print("not")


