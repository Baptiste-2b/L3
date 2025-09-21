
#%%

#imports
from typing import List, Dict

#exo 1 - Fonctions sur les chaînes de caractères

def nettoyer_espaces(chaine:str)->str:
    """Fonction pour supprimer les espaces en trop dans une chaîne (trim + espaces multiples)

    Args:
        chaine (str): chaîne d'origine

    Returns:
        str: chaîne nettoyée avec un seul espace entre les mots
    """
    # on coupe sur les espaces et on rejoint proprement
    mots = chaine.strip().split()
    return " ".join(mots)


def nb_caracteres(chaine:str, inclure_espaces:bool=True)->int:
    """Fonction pour compter le nombre de caractères d'une chaîne

    Args:
        chaine (str): chaîne d'origine
        inclure_espaces (bool, optional): True pour compter les espaces. Defaults to True.

    Returns:
        int: nombre de caractères
    """
    if inclure_espaces:
        return len(chaine)
    return len(chaine.replace(" ", ""))


def inverse_chaine(chaine:str)->str:
    """Fonction pour inverser une chaîne de caractères

    Args:
        chaine (str): chaîne d'origine

    Returns:
        str: chaîne inversée
    """
    return chaine[::-1]


def est_palindrome(chaine:str, ignorer_casse:bool=True, ignorer_espaces:bool=True)->bool:
    """Fonction pour déterminer si une chaîne est un palindrome

    Args:
        chaine (str): chaîne d'origine
        ignorer_casse (bool, optional): ignore la casse si True. Defaults to True.
        ignorer_espaces (bool, optional): ignore espaces et ponctuation simple si True. Defaults to True.

    Returns:
        bool: True si la chaîne est un palindrome
    """
    s = chaine
    if ignorer_casse:
        s = s.lower()
    if ignorer_espaces:
        # on garde uniquement les caractères alphanumériques
        s = "".join(ch for ch in s if ch.isalnum())
    return s == s[::-1]


def est_anagramme(a:str, b:str)->bool:
    """Fonction pour tester si deux chaînes sont des anagrammes

    Args:
        a (str): première chaîne
        b (str): deuxième chaîne

    Returns:
        bool: True si a et b sont des anagrammes (en ignorant espaces et casse)
    """
    ca = sorted(ch for ch in a.lower() if ch.isalnum())
    cb = sorted(ch for ch in b.lower() if ch.isalnum())
    return ca == cb


def occurrence_sous_chaine(chaine:str, sous_chaine:str)->int:
    """Fonction pour compter les occurrences (chevauchantes) d'une sous-chaîne

    Args:
        chaine (str): chaîne d'origine
        sous_chaine (str): motif à chercher

    Returns:
        int: nombre d'occurrences (avec chevauchements)
    """
    if not sous_chaine:
        return 0
    count = 0
    i = 0
    while True:
        i = chaine.find(sous_chaine, i)
        if i == -1:
            break
        count += 1
        i += 1  # autorise le chevauchement
    return count


def remplace_sous_chaine(chaine:str, ancien:str, nouveau:str)->str:
    """Fonction pour remplacer une sous-chaîne par une autre

    Args:
        chaine (str): chaîne d'origine
        ancien (str): motif à remplacer
        nouveau (str): motif de remplacement

    Returns:
        str: chaîne obtenue
    """
    return chaine.replace(ancien, nouveau)


def capitaliser_phrase(chaine:str)->str:
    """Fonction pour mettre une majuscule au début de chaque phrase

    Args:
        chaine (str): chaîne d'origine

    Returns:
        str: chaîne capitalisée phrase par phrase
    """
    res = []
    courant = ""
    ponct = ".!?"
    for ch in chaine.strip():
        courant += ch
        if ch in ponct:
            res.append(courant.strip().capitalize())
            courant = ""
    if courant.strip():
        res.append(courant.strip().capitalize())
    return " ".join(res)


def cesar(chaine:str, decalage:int)->str:
    """Fonction pour chiffrer une chaîne avec le chiffrement de César

    Args:
        chaine (str): chaîne d'origine
        decalage (int): décalage (positif pour décaler vers la droite)

    Returns:
        str: chaîne chiffrée
    """
    res = []
    d = decalage % 26
    for ch in chaine:
        if 'a' <= ch <= 'z':
            res.append(chr((ord(ch)-97 + d) % 26 + 97))
        elif 'A' <= ch <= 'Z':
            res.append(chr((ord(ch)-65 + d) % 26 + 65))
        else:
            res.append(ch)
    return "".join(res)


def trouver_mot_le_plus_long(chaine:str)->str:
    """Fonction pour trouver le mot le plus long d'une chaîne (séparateur espace)

    Args:
        chaine (str): chaîne d'origine

    Returns:
        str: mot le plus long, ou "" si aucun
    """
    mots = chaine.split()
    if not mots:
        return ""
    return max(mots, key=len)


def compte_mots(chaine:str)->Dict[str,int]:
    """Fonction pour compter les occurrences de chaque mot

    Args:
        chaine (str): texte d'origine

    Returns:
        Dict[str,int]: dictionnaire {mot: nombre d'occurrences}
    """
    occ = {}
    for mot in chaine.lower().split():
        mot = "".join(ch for ch in mot if ch.isalnum())
        if mot:
            occ[mot] = occ.get(mot, 0) + 1
    return occ


#fonction de test
def tester():
    """Fonction de test

    Returns:
        tuple: résultats des tests des fonctions chaînes
    """
    a = nettoyer_espaces("  Bonjour    le   monde   ")
    b = nb_caracteres("abc def", inclure_espaces=False)
    c = inverse_chaine("abcd")
    d = est_palindrome("Ésope reste ici et se repose")  # True
    e = est_anagramme("Chien", "Niche")
    f = occurrence_sous_chaine("aaaa", "aa")  # 3
    g = remplace_sous_chaine("lire et relire", "re", "RE")
    h = capitaliser_phrase("bonjour. comment ça va? tres bien!")
    i = cesar("Abc XyZ!", 3)
    j = trouver_mot_le_plus_long("un deux trois-quatre cinq")
    k = compte_mots("Un deux deux TROIS, trois TROIS!")
    return a, b, c, d, e, f, g, h, i, j, k
