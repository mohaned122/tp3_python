Mois=['janvier','Février','Mars','Avril','Mai','Juin','juillet','Aout','Septembre','Octobre','Novembre','Décember']
Nb_jours=[31,28,31,30,31,30,31,31,30,31,30,31]
T3=[]
print(Mois)
for m,n in zip(Mois,Nb_jours):
    T3.append(m)
    T3.append(n)

print(T3)