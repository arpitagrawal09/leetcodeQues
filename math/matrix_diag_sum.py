mat = [0, 1, 2, 3, 4]
mat[0] = [1, 1, 1, 1, 1]
mat[1] = [1, 1, 1, 1, 1]
mat[2] = [1, 1, 1, 1, 1]
mat[3] = [1, 1, 1, 1, 1]
mat[4] = [1, 1, 1, 1, 1]

l=len(mat)
isEven=False
if(l%2==0):
    isEven=True
sumPrimDiag=0
sumSecDiag=0
for i in range(l):
    sumPrimDiag+=mat[i][i]
for i in range(l):
    ele=mat[(l-1)-i][i]
    sumSecDiag+=ele

sumBrute = sumPrimDiag + sumSecDiag
sumFinal = 0
if(isEven==True):
    sumFinal = sumBrute
else:
    index_Mid = int(l/2) 
    sumFinal=sumBrute - mat[index_Mid][index_Mid]
print(sumFinal)