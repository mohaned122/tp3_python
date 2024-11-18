D = []
R = []
som = 0

while True:
    n = int(input("donnez la longeur de la liste: "))
    if n < 6 or n > 50:
        continue
    else:
        break

for i in range(n):
    x = int(input("donnez le nombre de case"))
    D.append(x)
    som += x
    R.append(som)

print(R)
print(D)
#****************************************************************
x=3,1415962
