a = input("Sirul: ")
rez = "a"
a = a.split()
for cuvant in a:
    rez = max(rez, cuvant)
print(rez)
