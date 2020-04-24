
List=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def heypaaah(lettre):
    a=List.index(lettre)
    return a

def dinosaure(mot):
    mot=mot.lower()
    L=[]
    for item in mot:
        a=heypaaah(item)
        L.append(a)
    return L

def tututu(L):
    LL=(L)
    ListC=[]
    Max=len(L)
    for i in range(Max):
        Min=min(LL)
        ListC.append(Min)
        LL.remove(Min)
    return ListC

def oulalaaa(nombre):
    L=[]
    for item in nombre:
        o=List[item]
        L.append(o)
    return L

def boomboom (mot):
    A=dinosaure(mot)
    B=tututu(A)
    C=oulalaaa(B)
    D=''.join(map(str,C))
    return D