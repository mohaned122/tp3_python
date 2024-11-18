matA = [[1,22,34],[3,34,4],[4,7,88]]
matB = [[10,5,19],[11,8,9],[4,6,6]]

print("*********addition**************")
for i in range(3):
    for j in range(3):
        print(matA[i][j]+matB[i][j],end=" ")
    print()

print("*********soustration**************")
for i in range(3):
    for j in range(3):
        print(matA[i][j]-matB[i][j],end=" ")
    print()

print("*********3A+10**************")
for i in range(3):
    for j in range(3):
        matA[i][j] = (3 * matA[i][j])+10
        print(matA[i][j], end=" ")
    print()

print("*********multiplication**************")
for i in range(3):
    for j in range(3):
        print(matA[i][j]*matB[i][j],end=" ")
    print()