Semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]

#medhode 1
for i in range(0,len(Semaine)):
    print(Semaine[i])

print("****************************")
#medhode 2
for i in Semaine:
    print(i)

A=["lundi","mardi"]
B=["mercredi","jeudi"]
C=["vendredi","samedi","dimanche"]
sept_jour = A + B + C
print(sept_jour)

sept_jour.pop()
sept_jour.pop()

print(sept_jour)