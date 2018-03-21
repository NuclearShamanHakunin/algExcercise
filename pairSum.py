niz1 = [12,5,2,-7,2,-11,3,7]
niz2 = [2,7,-14,8,6,10,-4]
niz3 = [1,-1,2,-2,3]

suma1 = 10
suma2 = 17

#TODO: ne nalazi sve kako treba
#problem1: Find pairs with given sum in the array
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

#problem2:  Check if subarray with 0 sum is exists or not
def daLiPostojiSumaNula(niz):
    for n in range(1,len(niz)+1,1): #n - number of elements
        for i in range(len(niz)):
            suma=0
            if i+1>n:
                continue
            for j in range(i,n,1):
                suma+=niz[j]
            if suma==0:
                return True
    return False

print(daLiPostojiSumaNula(niz3))
print(daLiPostojiSumaNula(niz1))

#problem3:   Find sub-array with 0 sum

def nizoviSaSumomNula(niz): #TODO: iz nekog razloga ne vraca sve podnizove
    tmpNiz=[]
    for n in range(1, len(niz) + 1, 1):  # n - number of elements
        for i in range(len(niz)):
            tmpPodNiz=[]
            suma = 0
            if i + 1 > n:
                continue
            for j in range(i, n, 1):
                suma += niz[j]
                tmpPodNiz.append(niz[j])
            if suma == 0:
                tmpNiz.append(tmpPodNiz)
    return tmpNiz

print((nizoviSaSumomNula(niz1)))
print((nizoviSaSumomNula(niz2)))
print((nizoviSaSumomNula(niz3)))

