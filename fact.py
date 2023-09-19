f=1
def fact(n):
    while n>=1:
        fac=f*n
        n=n-1
    return fac
a=int(input("enter a value"))
b=fact(a)
print(b)
    