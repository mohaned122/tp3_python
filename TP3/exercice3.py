min = int(input("Enter a number min: "))
max = int(input("Enter a number max: "))
som = 0
if min > max:
    min,max = max,min

for i in range(min,max+1):
    som+=i

print("somme de l'interval fermante ",min,",",max,"=",som)