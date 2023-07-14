#Leetcode problem 2011

X = 0
operations = ["X++", "++X", "--X", "X--", "X--"]
for i in range(len(operations)):
    operation = operations[i]
    if((operation=="X++") | (operation=="++X")):
        X = X + 1
    else : 
        X = X - 1
print(X)