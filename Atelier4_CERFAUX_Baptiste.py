
#%%

#imports
import random
import time
from typing import List, Tuple, Callable


#exercice 1 
def gen_list_random_int(n:int=10, int_binf:int=0, int_bsup:int=9)->list:
    """Fonction pour génerer une liste aléatoire de nombres entiers dans un intervalle donné

    Args:
        n (int, optional): Nombre de nombres. Defaults to 10.
        int_binf (int, optional): borne inférieur ( incluse ). Defaults to 0.
        int_bsup (int, optional): borne supérieure ( exclue ). Defaults to 9.

    Returns:
        list: Liste de nombres aléatoires
    """
    L = [random.randint(int_binf,int_bsup) for i in range(n)]
    return L


#exercice 2 
def mix_list(list_to_mix:list)->list:
    """Fonction pour mélanger une liste

    Args:
        list_to_mix (list): Liste à mélanger

    Returns:
        list: Liste mélangée
    """
    mixed_list=[]
    temp = list_to_mix
    for i in range(len(temp)):
        j = random.randint(0,len(temp)-1)
        mixed_list.append(temp[j])
        temp.pop(j)
    return mixed_list 


#exercice 3
def choose_element_list(list_in_which_to_choose:list)->int:
    """Fonction pour sortir un élément aléatoirement de ma liste

    Args:
        list_in_which_to_choose (list): Liste de base

    Returns:
        int: élément
    """
    temp = list_in_which_to_choose
    i = random.randint(0,len(temp)-1)
    return temp[i]


#exercice 4
def extract_elements_list(list_in_which_to_choose:list, int_nbr_of_element_to_extract:int)->list:
    """Fonction pour choisir n éléments aléatoirement dans une liste

    Args:
        list_in_which_to_choose (list): Liste de base
        int_nbr_of_element_to_extract (int): nombre d'éléments

    Returns:
        list: élément
    """
    L = []
    temp = list_in_which_to_choose
    n = int_nbr_of_element_to_extract
    for j in range(n):
        i = random.randint(0,len(temp)-1)
        L.append(temp[i])
        temp.pop(i)
    return L


def tri_selection(lst:List[int])->List[int]:
    """Fonction pour trier une liste par sélection

    Args:
        lst (List[int]): liste d'entiers

    Returns:
        List[int]: nouvelle liste triée
    """
    a = lst[:]  # on ne modifie pas la liste d'origine
    n = len(a)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a


def tri_insertion(lst:List[int])->List[int]:
    """Fonction pour trier une liste par insertion

    Args:
        lst (List[int]): liste d'entiers

    Returns:
        List[int]: nouvelle liste triée
    """
    a = lst[:]
    for i in range(1, len(a)):
        cle = a[i]
        j = i - 1
        while j >= 0 and a[j] > cle:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = cle
    return a


def tri_bulle(lst:List[int])->List[int]:
    """Fonction pour trier une liste par bulle

    Args:
        lst (List[int]): liste d'entiers

    Returns:
        List[int]: nouvelle liste triée
    """
    a = lst[:]
    n = len(a)
    for i in range(n):
        echange = False
        for j in range(0, n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                echange = True
        if not echange:
            break
    return a


def _fusion(gauche:List[int], droite:List[int])->List[int]:
    """Fonction pour fusionner deux listes triées

    Args:
        gauche (List[int]): partie gauche triée
        droite (List[int]): partie droite triée

    Returns:
        List[int]: liste résultante triée
    """
    res = []
    i, j = 0, 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            res.append(gauche[i]); i += 1
        else:
            res.append(droite[j]); j += 1
    res.extend(gauche[i:])
    res.extend(droite[j:])
    return res


def tri_fusion(lst:List[int])->List[int]:
    """Fonction pour trier une liste par fusion (merge sort)

    Args:
        lst (List[int]): liste d'entiers

    Returns:
        List[int]: nouvelle liste triée
    """
    n = len(lst)
    if n <= 1:
        return lst[:]
    m = n // 2
    gauche = tri_fusion(lst[:m])
    droite = tri_fusion(lst[m:])
    return _fusion(gauche, droite)


def _partition(a:List[int], debut:int, fin:int)->int:
    """Fonction pour partitionner un segment de liste (pivot final)

    Args:
        a (List[int]): liste d'entiers
        debut (int): indice début
        fin (int): indice fin

    Returns:
        int: position finale du pivot
    """
    pivot = a[fin]
    i = debut - 1
    for j in range(debut, fin):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[fin] = a[fin], a[i+1]
    return i + 1


def _tri_rapide_en_place(a:List[int], debut:int, fin:int)->None:
    """Fonction pour trier en place par rapide (quick sort)

    Args:
        a (List[int]): liste d'entiers
        debut (int): indice début
        fin (int): indice fin
    """
    if debut < fin:
        p = _partition(a, debut, fin)
        _tri_rapide_en_place(a, debut, p-1)
        _tri_rapide_en_place(a, p+1, fin)


def tri_rapide(lst:List[int])->List[int]:
    """Fonction pour trier une liste par rapide (wrapper non destructif)

    Args:
        lst (List[int]): liste d'entiers

    Returns:
        List[int]: nouvelle liste triée
    """
    a = lst[:]
    _tri_rapide_en_place(a, 0, len(a)-1)
    return a


def est_triee(lst:List[int])->bool:
    """Fonction pour vérifier si une liste est triée non décroissante

    Args:
        lst (List[int]): liste d'entiers

    Returns:
        bool: True si triée
    """
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))


def generer_liste_aleatoire(n:int, borne:int=1000)->List[int]:
    """Fonction pour générer une liste aléatoire d'entiers

    Args:
        n (int): taille de la liste
        borne (int, optional): valeur max (exclue). Defaults to 1000.

    Returns:
        List[int]: liste générée
    """
    return [random.randrange(borne) for _ in range(n)]


def mesurer_temps(f:Callable[[List[int]], List[int]], lst:List[int], repetitions:int=3)->float:
    """Fonction pour mesurer le temps moyen d'un algorithme de tri

    Args:
        f (Callable[[List[int]], List[int]]): fonction de tri
        lst (List[int]): liste à trier (de base)
        repetitions (int, optional): nombre de répétitions. Defaults to 3.

    Returns:
        float: temps moyen en secondes
    """
    # on recalcule à chaque fois sur une copie identique
    debut = time.perf_counter
    temps = []
    for _ in range(repetitions):
        a = lst[:]
        t0 = debut()
        _ = f(a)
        t1 = debut()
        temps.append(t1 - t0)
    return sum(temps) / len(temps)


def tester():
    """Fonction de test

    Returns:
        tuple: résultats de base des tris
    """
    base = [5, 2, 9, 1, 5, 6]
    a = tri_selection(base)
    b = tri_insertion(base)
    c = tri_bulle(base)
    d = tri_fusion(base)
    e = tri_rapide(base)
    f = est_triee(e)
    return a, b, c, d, e, f


def tester_perf():
    """Fonction de test pour mesurer les temps des tris

    Returns:
        dict: dictionnaire {nom_tri: temps_moyen}
    """
    lst = generer_liste_aleatoire(2000, 100000)
    mesures = {
        "selection": mesurer_temps(tri_selection, lst, repetitions=1),
        "insertion": mesurer_temps(tri_insertion, lst, repetitions=1),
        "bulle": mesurer_temps(tri_bulle, lst, repetitions=1),
        "fusion": mesurer_temps(tri_fusion, lst, repetitions=1),
        "rapide": mesurer_temps(tri_rapide, lst, repetitions=1),
    }
    return mesures