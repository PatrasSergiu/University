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
    

nr = int(input("Numar perechi: "))
perechi = []
for i in range(nr):
    stg = int(input("X sus= "))
    dr = int(input("Y sus= "))
    perechi.append((stg,dr))
    stg = int(input("X jos= "))
    dr = int(input("Y jos= "))
    perechi.append((stg,dr))

while perechi:
    nn = perechi.pop(0)
    mm = perechi.pop(0)
    print(nn,mm)
    suma = 0
    for i in range(nn[0]-1,mm[0]):
        for j in range(nn[1]-1,mm[1]): 
            suma += matrix[i][j] 
    print(suma)
