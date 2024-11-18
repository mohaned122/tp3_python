import math
min = 20
max = 40
lcarre =[]
lcube = []

for i in range(min,max+1):
    lcarre.append(i**2)
    lcube.append(i**3)

print(lcarre)
print(lcube)

liste5=[x**5 for x in range(6,15)]
print(liste5)

lsin = [math.sin(x) for x in range(0,91,5)]
print(lsin)