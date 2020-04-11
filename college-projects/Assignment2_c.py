Numbers=[1,2,3,4,5,6,7,8,9,10]
num = []
m=0
c=int(input("Enter a choice:\n1)Sum of first 10 numbers\n2)Sum of 10 input numbers using for loop:\n"))
if c==1:
   print(sum(Numbers))
else:
    for i in range(1,11):
        num1 = int(input("Enter num:"))
        num.append(num1)
print(sum(num))
