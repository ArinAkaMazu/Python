def fact(n):
    factorial=1
    for i in range(1,11):
        factorial=i*i
    return factorial
n=int(input("enter a number"))
final=fact(n)
print(final)