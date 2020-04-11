alphabet=list('abcdefghijklmnopqrstuvwxABCDEFGHIJKLMNOPQRST')
numbers=list('1234567890')
characters=list('@$%&')
string=input("Enter password:")
n=len(string)
flag1=0
flag2=0
flag3=0

if n>5 and n<16:
    for i in string:
        if i in alphabet:
            flag1=1
        if i in numbers:
            flag2=1
        if i in characters:
            flag3=1
    if flag1==1 and flag2==1 and flag3==1:
        print("Password is strong and valid!")
    else:
        print("Password is weak. Please try again!")

else:
    print("Password out of range bounds. Please try again with length of more than 5 and less than 15 characters!")
