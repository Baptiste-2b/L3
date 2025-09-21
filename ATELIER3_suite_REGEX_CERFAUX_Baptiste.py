
#%%

#imports
import re
from typing import List, Dict, Tuple

#exo 1 - Expressions régulières (REGEX)

def valider_email(email:str)->bool:
    """Fonction pour valider un email simple avec REGEX

    Args:
        email (str): email d'origine

    Returns:
        bool: True si l'email est valide
    """
    motif = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.fullmatch(motif, email) is not None


def valider_telephone_fr(numero:str)->bool:
    """Fonction pour valider un numéro français (0X XX XX XX XX, +33X...)

    Args:
        numero (str): numéro d'origine

    Returns:
        bool: True si le numéro est valide
    """
    motif = r"^(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}$"
    return re.fullmatch(motif, numero) is not None


def valider_code_postal_fr(cp:str)->bool:
    """Fonction pour valider un code postal français à 5 chiffres

    Args:
        cp (str): code postal

    Returns:
        bool: True si le code postal est valide
    """
    return re.fullmatch(r"^\d{5}$", cp) is not None


def extraire_dates_fr(texte:str)->List[str]:
    """Fonction pour extraire les dates au format JJ/MM/AAAA

    Args:
        texte (str): texte d'origine

    Returns:
        List[str]: liste des dates trouvées
    """
    motif = r"\b(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/(\d{4})\b"
    return re.findall(motif, texte) and ["/".join(t) for t in re.findall(motif, texte)] or []


def extraire_urls(texte:str)->List[str]:
    """Fonction pour extraire les URLs (http/https)

    Args:
        texte (str): texte d'origine

    Returns:
        List[str]: liste des URLs
    """
    motif = r"https?://[^\s)]+"
    return re.findall(motif, texte)


def extraire_hashtags(texte:str)->List[str]:
    """Fonction pour extraire les hashtags style #Python

    Args:
        texte (str): texte d'origine

    Returns:
        List[str]: liste des hashtags
    """
    return re.findall(r"#[A-Za-z0-9_]+", texte)


def nettoyer_html(texte:str)->str:
    """Fonction pour supprimer les balises HTML simples

    Args:
        texte (str): texte d'origine

    Returns:
        str: texte sans balises
    """
    # supprime les balises <...>
    sans_balises = re.sub(r"<[^>]+>", "", texte)
    # compresse les espaces
    return " ".join(sans_balises.split())


def password_strength(mot_de_passe:str)->bool:
    """Fonction pour vérifier la force d'un mot de passe (règles de base)

    Args:
        mot_de_passe (str): mot de passe

    Returns:
        bool: True si le mot de passe respecte les règles
    """
    if len(mot_de_passe) < 8:
        return False
    tests = [
        re.search(r"[a-z]", mot_de_passe),
        re.search(r"[A-Z]", mot_de_passe),
        re.search(r"\d", mot_de_passe),
        re.search(r"[^A-Za-z0-9]", mot_de_passe),
    ]
    return all(tests)


def remplacer_multi_espaces(texte:str)->str:
    """Fonction pour remplacer les suites d'espaces par un seul

    Args:
        texte (str): texte d'origine

    Returns:
        str: texte avec espaces normalisés
    """
    return re.sub(r"\s+", " ", texte).strip()


def couper_mots(texte:str)->List[str]:
    """Fonction pour découper les mots en utilisant REGEX (séparateurs non-alphanum)

    Args:
        texte (str): texte d'origine

    Returns:
        List[str]: liste des mots (vides exclus)
    """
    morceaux = re.split(r"\W+", texte, flags=re.UNICODE)
    return [m for m in morceaux if m]


#fonction de test
def tester():
    """Fonction de test

    Returns:
        tuple: résultats des tests des fonctions REGEX
    """
    a = valider_email("prenom.nom@example.com")
    b = valider_telephone_fr("06 12 34 56 78")
    c = valider_code_postal_fr("75001")
    d = extraire_dates_fr("Rdv le 01/03/2025 et le 12/11/2024.")
    e = extraire_urls("Visiter http://exemple.com et https://site.org/page")
    f = extraire_hashtags("#Python #regex #AI_2025!")
    g = nettoyer_html("<p>Bonjour <b>le</b> monde</p>")
    h = password_strength("Abcdef1!")
    i = remplacer_multi_espaces("Texte   avec\tbeaucoup\n  d'espaces   ")
    j = couper_mots("Bonjour, le-monde! 42 fois.")
    return a, b, c, d, e, f, g, h, i, j
