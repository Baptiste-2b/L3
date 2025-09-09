#%%

#fonction de test
def tester():
    """Fonction de test

    Returns:
        _type_: résultats des tests des fonctions de l'exo 1
    """
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
    """Fonction pour calculer la valeur moyenne d'une liste

    Args:
        ma_liste (list): liste d'origine

    Returns:
        float: valeur de la moyenne
    """
    somme = 0
    i = 0
    for i in range (0, len(ma_liste)):
        somme += ma_liste[i]
    return somme / len(ma_liste)

def nb_sup_fori(ma_liste:list, element:int)->list:
    """Fonction pour trouver le nb d'éléments d'une liste au dessus d'un certain élément avec une boucle FOR i IN RANGE

    Args:
        ma_liste (list): liste d'origine
        element (int): élémént seuil

    Returns:
        list: liste des éléments au dessus du seuil
    """
    i = 0
    L = []
    k = 0
    for i in range (0, len(ma_liste)):
        if ma_liste[i] > element :
            k += 1
            L.append(ma_liste[i])
    return (L, k)

def nb_sup_forE(ma_liste:list, element:int)->list:
    """Fonction pour trouver le nb d'éléments d'une liste au dessus d'un certain élément avec une boucle FOR e IN liste

    Args:
        ma_liste (list): liste d'origine
        element (int): élémént seuil

    Returns:
        list: liste des éléments au dessus du seuil
    """
    L=[]
    for E in ma_liste:
        if E > element :
            L.append(E)
    return L

def nb_sup_forW(ma_liste:list, element:int)->list:
     """Fonction pour trouver le nb d'éléments d'une liste au dessus d'un certain élément avec un WHILE

    Args:
        ma_liste (list): liste d'origine
        element (int): élémént seuil

    Returns:
        list: liste des éléments au dessus du seuil
    """
     n = len(ma_liste)
     i = 0
     L = []
     while i < n :
        if ma_liste[i] > element :
            L.append(ma_liste[i])
        i+=1
     return L

def moy_sup(ma_liste:list, elt:int)->float:
    """Fonction pour calculer la moyenne au dessus d'un seuil

    Args:
        ma_liste (list): liste d'origine
        elt (int): seuil

    Returns:
        float: valeur de la moyenne
    """
    S = nb_sup_forE(ma_liste, elt)
    M = moyenne_dune_lst(S)
    return M

def val_max(lst:list)->float:
    """Fonction de maximum d'une liste

    Args:
        lst (list): liste d'origine

    Returns:
        float: le maximum
    """
    m = lst[0]
    i = 0
    for i in range (1, len(lst)):
        if lst[i] > m :
            m = lst[i]
    return m

def ind_max(lst:list)->int:
    """Fonction pour l'indice du maximum de la liste

    Args:
        lst (list): liste d'origine

    Returns:
        int: indice du max
    """
    m = val_max(lst)
    return lst.index(m)

#%%

#fonction de test
def tester2():
    """Fonction de test

    Returns:
        _type_: résultats des tests des fonctions de l'exo 2
    """
    a = position1([1, 4, 7, 10, 3, 45, 2, 2, 9], 5)
    b = position2([1, 4, 7, 10, 3, 45, 2, 2, 9], 9)
    c = nb_occurrences([1, 4, 7, 10, 3, 45, 2, 2, 9], 2)
    return a, b, c

#exo2

def position1(lst:list, elt:int)->float:
    """Fonction pour trouver la position d'un élément dans une liste avec boucle FOR

    Args:
        lst (list): liste d'origine 
        elt (int): élément 

    Returns:
        float: élément si IN ou alors -1
    """
    i=0
    for i in range(0, len(lst)):
        if lst[i] == elt :
            return i
    return -1

def position2(lst:list, elt:int)->float:
    """Fonction pour trouver la position d'un élément dans une liste avec boucle WHILE

    Args:
        lst (list): liste d'origine 
        elt (int): élément 

    Returns:
        float: élément si IN ou alors -1
    """
    i = 0
    while i < len(lst):
        if lst[i] == elt :
            return i
        i += 1
    return -1

def nb_occurrences(lst:list, e:int)->int:
    """Fonction pour avoir le nombre d'occurences d'un élément dans une liste

    Args:
        lst (list): liste d'origine
        e (int): élément

    Returns:
        int: nombre d'occurences
    """
    i = 0
    occ = 0
    for i in range(0, len(lst)):
        if lst[i] == e :
            occ += 1
    return occ

#%%

#fonction de test
def tester3():
    """Fonction de test

    Returns:
        _type_: résultats des tests des fonctions de l'exo 3
    """
    a = separer([-2, 8, 0, 4, 7, -1000, 3, 0, 0, 2, -6])
    return a

#exo 3

def separer(lst:list):
    """Fonction de séparation de liste

    Args:
        lst (list): liste d'origine

    Returns:
        _type_: négatifs à gauche, zéros au milieu, positifs à droite
    """
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
def tester4():
    """Fonction de test

    Returns:
        _type_: résultats des tests des fonctions de l'exo 4
    """
    a = fizzBuzz(12)
    return a

#exo 4
def fizzBuzz(n:int)->str:
    """Fonction pour le jeu FizzBuzz

    Args:
        n (int): nombre choisi pour le fizzbuzz

    Returns:
        str: déroulement du jeu : 
            Fizz si le nombre est multiple de 3 ;
            Buzz si le nombre est multiple de 4 ;
            FizzBuzz si le nombre est à la fois multiple de 3 et de 4;
            i si aucune des conditions n est vérifiée.
    """
    i = 0
    for i in range (1, n+1) :
        if i % 3 == 0 and i % 4 == 0 :
            print ("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 4 == 0:
            print("Buzz")
        else :
            print(i)

#%%

#fonction de test
def tester5():
    """Fonction de test

    Returns:
        _type_: résultats des tests des fonctions de l'exo 5
    """
    d_quantite = {"500_euro":5, "200_euro":200,"100_euro":0, "50_euro":5,
            "20_euro":20, "10_euro":0, "5_euro":500, "2_euro":70, "1_euro":0, 
            "50_centime":0, "20_centime":20, "10_centime":8, "5_centime":0, 
            "2_centime":200, "1_centime":120}
    a = renduMonnaie(201.95, d_quantite)
    return a

#exo 5
def renduMonnaie(argent:float, billetsDispo:dict)->list:
    """Fonction de rendu de monnaie basique

    Args:
        argent (float): argent à rendre
        billetsDispo (dict): nombre de billets disponibles pour chaque espèce

    Returns:
        list: liste des espèces rendues
    """
    prix = {"500_euro":50000, "200_euro":20000,"100_euro":10000, "50_euro":5000,
            "20_euro":2000, "10_euro":1000, "5_euro":500, "2_euro":200, "1_euro":100, 
            "50_centime":50, "20_centime":20, "10_centime":10, "5_centime":5, 
            "2_centime":2, "1_centime":1}
    result = []
    temp:int = argent * 100
    temp2:int = argent * 100
    while temp != 0:
        for i in prix.keys():
            if billetsDispo[i] != 0 and prix[i] <= temp :
                temp2 = min(temp - prix[i], temp2)
        result.append((temp - temp2)/100)  
        temp = temp2
    return result 

#%%

#fonction de test
def tester6():
    """Fonction de test

    Returns:
        _type_: résultats des tests des fonctions de l'exo 6
    """
    l = [1,2,2,2,3,5,6,9,9,3,8]
    a = vitrine(3,l)
    return a
    
#exo 6
def vitrine(nbEmplacement:int, lObjets:list)->list:
    """Fonction de représentation d'une vitrine

    Args:
        nbEmplacement (int): nombre d'emplacements disponibles dans la vitrine
        lObjets (list): liste des objets à exposer

    Returns:
        list: liste des objets exposés selon les règles
    """
    L = []
    G = []
    for i in lObjets :
        if i not in L and len(L) < nbEmplacement + 1 :
            L.append(i)
        else :
            G.append(i)
    if len(G) == 0 :
        return L
    else : 
        return L, vitrine(nbEmplacement, G)

#%%

#imports
from random import randint

#fonction de test
def tester8():
    """Fonction de test

    Returns:
        _type_: résultats des tests des fonctions de l'exo 8
    """
    return tennis()

#exo 8
def tennis()->str:
    """Fonction pour simuler une partie de Tennis 

    Déroulé :
        1. Les points dans un jeu

    Un jeu se gagne en marquant au moins 4 points avec 2 points d écart.
    Le comptage se fait de façon particulière :

    0 point → 0

    1 point → 15

    2 points → 30

    3 points → 40

    4 points (si 2 d avance) → Jeu

    👉 Exemple :

    40 à 30 → le joueur à 40 gagne le point → jeu.

    40 à 40 → égalité (deuce).

    2. L égalité (deuce) et l avantage

    À 40 à 40, on dit égalité.

    Le joueur qui marque le point suivant obtient “avantage”.

    Si le joueur à l avantage gagne encore un point → jeu.

    Si l autre joueur gagne le point → retour à égalité.

    3. Les jeux dans un set

    Un set se gagne en remportant 6 jeux avec 2 jeux d écart (par ex. 6 à 4).

    Si les deux joueurs sont à 5 à 5 → il faut aller à 7 à 5.

    Si les deux joueurs arrivent à 6 6 → on joue un tie-break (sauf certaines compétitions comme Roland-Garros avant 2022 où il fallait 2 jeux d écart même au-delà de 6 6).

    4. Le tie-break

    Le tie-break se joue généralement en 7 points avec 2 points d écart.

    Le score se compte 1, 2, 3… (et non 15 30 40).

    Le vainqueur du tie-break gagne le set 7 6.

    Returns:
        str: Gagnant avec nombre de jeux
    """
    table=[0, 15, 30, 40, "40 + 1", "40 + 2", "40 + 3", "40 + 4", "40 + 5", "40 + 6", "40 + 7", "40 + 8", "40 + 9"]
    points_P1, points_P2, jeu_P1, jeu_P2 = 0, 0, 0, 0
    match_set = True
    while match_set is True :
        choix_point = randint(0,1)
        if choix_point == 0 :
            points_P1 += 1
            print ("Le joueur 1 marque 1 point :", table[points_P1]) 
        else :
            points_P2 += 1
            print ("Le joueur 2 marque 1 point :", table[points_P2])
        if ( points_P1 >= 4 or points_P2 >= 4 ) and abs(points_P1 - points_P2) >= 2 :
            if max(points_P1, points_P2) == points_P1 : 
                jeu_P1 += 1
                print ("Le joueur 1 marque 1 jeu :", jeu_P1, "|", table[points_P1], "-", table[points_P2])
                points_P1, points_P2 = 0, 0
            else : 
                jeu_P2 += 1 
                print ("Le joueur 2 marque 1 jeu :", jeu_P2, "|", table[points_P1], "-", table[points_P2])
                points_P1, points_P2 = 0, 0
        if ( jeu_P1 >= 6 or jeu_P2 >= 6 ) and abs(jeu_P1 - jeu_P2) >= 2 :
            match_set = False
            if max(jeu_P1, jeu_P2) == jeu_P1 : 
                return "Le joueur 1 gagne", jeu_P1, "à", jeu_P2
            else : 
                return "Le joueur 2 gagne", jeu_P1, "à", jeu_P2
        if jeu_P1 == 6 and jeu_P2 == 6 :
            points_P1, points_P2 = 0, 0
            tie_break = True
            while tie_break is True :
                choix_point = randint(0,1)
                if choix_point == 0 :
                    points_P1 += 1
                    print ("Le joueur 1 marque 1 point", points_P1)
                else :
                    points_P2 += 1
                    print ("Le joueur 2 marque 1 point", points_P1)
                if ( points_P1 >= 7 or points_P2 >= 7 ) and abs(points_P1 - points_P2) >= 2 :
                    tie_break = False
                    if max(points_P1, points_P2) == points_P1 : 
                        return "Le joueur 1 gagne", jeu_P1, "à", jeu_P2
                    else : 
                        return "Le joueur 1 gagne", jeu_P1, "à", jeu_P2


#%%

#fonction de test
def tester9():
    """Fonction de test

    Returns:
        _type_: résultats des tests des fonctions de l'exo 9
    """
    return eval_polynome(2, 4, 2, 3, 7, 8, 1), eval_polynome_mieux(2, 4, 2, 3, 7, 8, 1)
    
#exo 9 
def eval_polynome(a0:int, a1:int, a2:int, a3:int, a4:int, a5:int, x:int)->int:
    """Fonction pour évaluer un polynôme de manière basique

    Commentaire : 
    (n+1)(n+2)/2 multiplications et n additions

    Args:
        a0 (int): coeff
        a1 (int): coeff
        a2 (int): coeff
        a3 (int): coeff
        a4 (int): coeff
        a5 (int): coeff
        x (int): valeur de x

    Returns:
        int: résultat 
    """
    return (a5*x**5 + a4*x**4 + a3*x**3 + a2*x**2 + a1*x**1 + a0*x**0)
    
def eval_polynome_mieux(a0:int, a1:int, a2:int, a3:int, a4:int, a5:int, x:int)->int:
    """Fonction pour évaluer un polynôme avec la forme de Horner

    Commentaire : 
    n multiplications et n additions

    Args:
        a0 (int): coeff
        a1 (int): coeff
        a2 (int): coeff
        a3 (int): coeff
        a4 (int): coeff
        a5 (int): coeff
        x (int): valeur de x

    Returns:
        int: résultat 
    """
    return (a0 + x*(a1 + x*(a2 + x*(a3 + x*(a4 + x*a5)))))
    

#%%

texte = "bonjour bonjour salut"
compte = {}
for mot in texte.split():
    compte[mot] = compte.get(mot,0) + 1
    
print(compte)
print(compte.get("oui"))   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
  