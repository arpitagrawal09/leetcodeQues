""" str1 = "America"
str2 = "Amer"

if(str1[1]==str2[1]):
    print("good first success") """

haystack = "simsimpolapola"
needle = "simpola"
i = -1
lh = len(haystack)
ln = len(needle)
for i in range(lh):
    if(needle[0]==haystack[i]):
        if(needle==haystack[i:(i+ln)]):
            print("What a coincidence!, the needle can be found at the index "+str(i))
            break

""" paraya = "America"
apna = paraya[0:4]
print(apna)
 """

