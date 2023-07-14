#Author : Arpit Agrawal     Date : 12/05/2023 

romanVal = "LVIII"
decimalVal = 0
#romanSet = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

for i in range(len(romanVal)):
    
    if(romanVal[i]=="M"):
        decimalVal+=1000
    if(romanVal[i]=="D"):
        decimalVal+=500
    if(romanVal[i]=="C"):
        decimalVal+=100
    if(romanVal[i]=="L"):
        decimalVal+=50
    if(romanVal[i]=="X"):
        decimalVal+=10
    if(romanVal[i]=="V"):
        decimalVal+=5
    if(romanVal[i]=="I"):
        decimalVal+=1
print(decimalVal)
            