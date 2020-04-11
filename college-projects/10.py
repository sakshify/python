num=int(input("Enter a number to display it's divisors: "))

lstRange = list(range(1,num+1))

divisorList = []

for number in lstRange:
    if num % number == 0:
        divisorList.append(number)

print("Divisors=\n",divisorList)