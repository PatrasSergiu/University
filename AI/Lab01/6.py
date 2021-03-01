from collections import Counter
array = []
n = int(input("N ="))

for i in range(0,n):
    array.append(input("x[i]="))
output = Counter(array)
found = False
for x in output:
    if output[x] > n//2:
        print(x)
        found = True;

if not found:
    print("Nu exista element majoritar")
