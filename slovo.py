way = "prim.txt"
filt = dict()
with open (way , "r")as f: 
    stroki =str(f.read())
    slova = stroki.lower().split()
    for char in range(len(slova)):
        slovo = slova[char]
        filt[slovo] = filt.get(slovo ,0) +1
NURBOLAT = max(filt , key= filt.get)
print (NURBOLAT) # kazah