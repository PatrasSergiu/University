n = int(input("Dimensiune vector: "))


a = []
b = []

for i in range(n):
    a.append(int(input("a[i]= ")))
for i in range(n):
    b.append(int(input("b[i]= ")))

output = 0
for i in range(n):
    output += a[i]*b[i]

print(output)
