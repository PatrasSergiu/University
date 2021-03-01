from collections import Counter
s = input("Sir: ")
s = s.split()
output = Counter(s)
for x in output:
    if(output[x]==1):
        print(x)

