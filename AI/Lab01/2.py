from math import sqrt
x = int(input("X1 = "))
y = int(input("Y1 = "))
p1 = (x,y)
x = int(input("X2 = "))
y = int(input("Y2 = "))
p2 = (x,y)

print(sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2))
