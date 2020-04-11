num = int(input("Enter a number to check if Armstrong or not:"))
temp = num
n = 0
while (num > 0):
    a = num % 10
    n = n + (a * a * a)
    num = num // 10

if (n == temp):
    print("The number is armstrong number!")
else:
    print("The number is not armstrong number!")
