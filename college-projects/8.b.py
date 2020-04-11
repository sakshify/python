num = int(input("Enter a number to check palindrome:"))
a=num
temp=num
new=0
for a in range(0,len(str(num))):
	new=new+num%10
	num=num//10
	new=new*10

new=new//10

if new==temp:print("It is palindrome!")

else:print("It is not palindrome!")
