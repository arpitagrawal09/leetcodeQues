# https://leetcode.com/problems/pascals-triangle/   Pascals Triangle 

def pascalsTriangle(numRows):
    pT = [[1]]
    n = numRows

    for i in range(1, n):
        row = [1]
        rowPrev = pT[i-1]
        for j in range(1, i):
            iLeft = j-1
            iSame = j
            ele = rowPrev[iLeft] + rowPrev[iSame]
            row.append(ele)
        row.append(1)
        pT.append(row)

    return pT

numRows = 7
pT = pascalsTriangle(numRows)
print(pT)