num=[]
flag=0
num1=int(input("Enter number of digits"))
no=num1-1
for i in range(0,num1,1):
    n=int(input("Enter a string of numbers"))
    num.append(n)
for i in range(0,no,1):
    for j in range(no,0,-1):
        if(num[i]==num[j]):
            flag=1
        else:
            flag=0

            break
if(flag==1):
    print("Palindrome!")
else:
    print("Not palindrome")