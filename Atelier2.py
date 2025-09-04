#%%

#fonction de test
def tester():
    a = moyenne_dune_lst([1, 4, 7, 10, 3, 45, 2, 2, 9])
    b = nb_sup_fori([1, 4, 7, 10, 3, 45, 2, 2, 9], 5)
    c = nb_sup_forE([1, 4, 7, 10, 3, 45, 2, 2, 9], 5)
    d = nb_sup_forW([1, 4, 7, 10, 3, 45, 2, 2, 9], 5)
    e = moy_sup([1, 4, 7, 10, 3, 45, 2, 2, 9], 5)
    f = val_max([1, 4, 7, 10, 3, 45, 2, 2, 9])
    g = ind_max([1, 4, 7, 10, 3, 45, 2, 2, 9])
    return a, b, c, d, e, f, g

#exo1
def moyenne_dune_lst(ma_liste:list)->float:
    somme = 0
    i = 0
    for i in range (0, len(ma_liste)):
        somme += ma_liste[i]
    return somme / len(ma_liste)

def nb_sup_fori(ma_liste:list, element:int)->list:
    i = 0
    L = []
    for i in range (0, len(ma_liste)):
        if ma_liste[i] > element :
            L.append(ma_liste[i])
    return L

def nb_sup_forE(ma_liste:list, element:int)->list:
    L=[]
    for E in ma_liste:
        if E > element :
            L.append(E)
    return L

def nb_sup_forW(ma_liste:list, element:int)->list:
    n = len(ma_liste)
    i = 0
    L = []
    while i < n :
        if ma_liste[i] > element :
            L.append(ma_liste[i])
        i+=1
    return L

def moy_sup(ma_liste:list, elt:int)->float:
    S = nb_sup_forE(ma_liste, elt)
    M = moyenne_dune_lst(S)
    return M

def val_max(lst:list)->float:
    m = lst[0]
    i = 0
    for i in range (1, len(lst)):
        if lst[i] > m :
            m = lst[i]
    return m

def ind_max(lst:list)->int:
    m = val_max(lst)
    return lst.index(m)

#%%

#fonction de test
def tester2():
    a = position1([1, 4, 7, 10, 3, 45, 2, 2, 9], 5)
    b = position2([1, 4, 7, 10, 3, 45, 2, 2, 9], 9)
    c = nb_occurrences([1, 4, 7, 10, 3, 45, 2, 2, 9], 2)
    return a, b, c

#exo2

def position1(lst:list, elt:int)->float:
    i=0
    for i in range(0, len(lst)):
        if lst[i] == elt :
            return i
    return -1

def position2(lst:list, elt:int)->float:
    i = 0
    while i < len(lst):
        if lst[i] == elt :
            return i
        i += 1
    return -1

def nb_occurrences(lst:list, e:int)->int:
    i = 0
    occ = 0
    for i in range(0, len(lst)):
        if lst[i] == e :
            occ += 1
    return occ

#%%

#fonction de test
def tester3():
    a = separer([-2, 8, 0, 4, 7, -1000, 3, 0, 0, 2, -6])
    return a

#exo 3

def separer(lst:list):
    L = []
    i = 0
    k = 0
    for i in range (0, len(lst)):
        if lst[i] > 0:
            L.append(lst[i])
        elif lst[i] < 0:
            L.insert(0, lst[i])
            k += 1
        else : 
            L.insert(k, lst[i])
    return L
            
#%%

#fonction de test
def fizzBuzz(n:int)->str:
    i = 0
    for i in range (1, n) :
        
        
