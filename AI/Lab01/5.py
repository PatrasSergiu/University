n = int(input("N=  "))
sir=[]
for x in range(n+1):
    nr = int(input("n: "))
    sir.append(nr)

for x in range(n+1):
    if sir[x] != x+1:
        print(sir[x])
        break
