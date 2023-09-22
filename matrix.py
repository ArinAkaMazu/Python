n=int(input("Enter number of rows"))
m=int(input("Enter number of columns"))
matrix=[]
print("enter the values \n")
for i in range (n):
    data=[]
    for j in range(m):
        data.append(int(input()))
    matrix.append(data)
    print()
for i in range(n):
    for j in range(m):
        print(matrix[i][j])
    print()
for i in range(n):
    sum=0
    for j in range(m):
        sum=sum+matrix[i][j]
    print("sum of row",i+1,"is",sum)
    print()