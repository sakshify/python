a=int(input())
b=int(input())
c = int(input("Enter choice:"))
switcher = {
    1:(a+b),
    2:(a-b),
    3:(a*b),
    4:(a/b),
    5:(a%b),
    6:(pow(a,b)),
}
print(switcher[c])