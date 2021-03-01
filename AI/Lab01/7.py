array = []
n = int(input("N ="))

for i in range(0,n):
    array.append(int(input("x[i]=")))

array.sort(reverse=True)
print(array[1])
