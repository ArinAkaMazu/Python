data=[("abc",29,159999),
      ("pqr",21,59999),
      ("xyz",15,743545)]
sal=lambda salary:(salary[0],salary[2]*2)
updated=list(map(sal,data))
for i in updated:
    print(i)