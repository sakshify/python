def reverse(st):
    if len(st)==0:
        return st
    else:
        return reverse(st[1:]) + st[0]
def palindrome(st):
     rev=reverse(st)
     if st==rev:
         print("Palindrome")
     else:
         print('Not Palindrome!')
def checkst1(st):
    st1 = str(input("Enter substring:"))
    if st.find(st1)==-1:
            print("Does not exist!")
    else:
            print("Exists!")
def frequency(st):
       i=0
       j=len(st)
       d=str(input("Enter a char"))
       if st.find(d)!=-1:
               i = i + 1

       print("Frequency=",i)

st=str(input("Enter a string:"))
c=int(input("Enter choice:\n1)Length\n2)String Reverse\n3)Palindrome\n4)Occurrence of substring\n5)Frequency of a char\n"))
switch = {
     1: print("Length of the entered string= ",len(st)),
     2: print(reverse(st)),
     3: palindrome(st),
     4: checkst1(st),
     5: frequency(st),
}
print(switch[c])