n = int(input("N ="))
m = int(input("M ="))

matrix = []
for i in range(n):
    a = []
    for j in range(m):
        a.append(int(input("a[i][j] = ")))
    matrix.append(a)
print("Matricea citita: ")
for i in range(n):
    for j in range(m): 
        print(matrix[i][j], end = " ") 
    print()

maxim = 0

for i in range(n):
    if sum(matrix[maxim]) < sum(matrix[i]):
        maxim = i

print("A ", maxim+1, " a linie")
