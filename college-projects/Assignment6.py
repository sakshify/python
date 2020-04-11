num=[]
for i in range(0,3,1):
    n = int(input("Enter a number:"))
    num.append(n)
if(num[0]>num[1] & num[0]>num[2]):
   print("Maximum number=",num[0])
elif(num[1]>num[0] & num[1]>num[2]):
    print("Maximum number=",num[1])
else:
    print("Maximum number=", num[2])