#Find pair with given sum in the array

niz1 = [12,5,2,7,2,11,3]
niz2 = [2,7,14,8,6,10,-4]

suma1 = 10
suma2 = 17

def nadjiParoveSaSumom(niz,suma):
    tmpDict={}
    for i in range(len(niz)):
        for j in range(len(niz)-1):
            if i==j:
                continue
            if niz[i]+niz[j]==suma:
                if niz[j] in tmpDict:
                    continue
                else:
                    tmpDict.update({niz[i]:niz[j]})
    return tmpDict

a=nadjiParoveSaSumom(niz1,suma1);print(a)
b=nadjiParoveSaSumom(niz2,suma1);print(b)
c=nadjiParoveSaSumom(niz1,suma2);print(c)
d=nadjiParoveSaSumom(niz2,suma2);print(d)
