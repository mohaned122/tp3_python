x = float(input("Enter a number: "))
stro = str(x)
n = int(input("donnez les nombre apres vérgule: "))
l=[]
k=[]
for i in range(n):
    x = (x*10)%10
    l.append(int(x))


for i in range(2,len(stro)+2):
    k.append(stro[i])
print(l)
print(k)