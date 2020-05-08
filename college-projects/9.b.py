str=[]
string='p'
i=0
while string!=' ':
    string = input("Enter a string of lines. Give <space> as input to terminate.")
    str.append(string)
    i+=1
print("String in lowercase=")
for k in range(0,i):
    print(str[k].lower())
    ###hiiiiiiiiiiiiii
