n=int(input("Enter a number"))
flag=0
for i in range(2,n,1):
    if(n%i==0):
        flag=1
        break
if(flag==0):
    print("It's a prime number")
else:
    print("It's not a prime number")