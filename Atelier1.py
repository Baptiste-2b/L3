#imports
from math import sqrt

#exo 1
def message_imc(imc:float)->str:
    """Fonction pour afficher s'informer sur sa condition par l'imc

    Args:
        imc (float): variable pour stocker l'imc

    Returns:
        str: message informant de sa condition
    """
    
    if imc < 0 :
        return "mauvaise imc, veuillez réessayer"
    elif imc < 16.5:
        return "dénutrition ou famine"
    elif imc < 18.5 :
        return "maigreur"
    elif imc < 25 :
        return "corpulence normale"
    elif imc < 30 :
        return "surpoids"
    elif imc < 35 : 
        return "obésité modérée"
    elif imc < 40 :
        return "obésité sévère"
    else :
        return "obésité morbide"

#exo 2    
def est_bissextile(annee:int)->bool:
    """Fonction pour déterminer si une année est bissextile

    Args:
        annee (int): Variable pour stocker l'année

    Returns:
        bool: True / False pour savoir si on est une année bissextile ou non
    """
    result_4 = annee % 4
    result_100 = annee % 100
    result_400 = annee % 400
    if result_4 == 0 and result_100 == 0 or result_400 == 0:
        return True
    else : 
        return False

#exo 3
def distance_points_3d(x_a:int, y_a:int, z_a:int, x_b:int, y_b:int, z_b:int)->float:
    """Fonction pour calculer la distance entre deux points en 3d

    Args:
        x_a (int): coordonnée x du point A
        y_a (int): coordonnée y du point A
        z_a (int): coordonnée z du point A
        x_b (int): coordonnée x du point B
        y_b (int): coordonnée y du point B
        z_b (int): coordonnée z du point B

    Returns:
        float: Renvoie la distance calculée
    """
    x = (x_b - x_a)**2 + (y_b - y_a)**2 + (z_b - z_a)**2
    return sqrt(x)

#exo 4
def est_triangle(a:int, b:int, c:int)->bool:
    """Fonction pour savoir si 3 segments peuvent former un triangle

    Args:
        a (int): longueur du segment A
        b (int): longueur du segment B
        c (int): longueur du segment C

    Returns:
        bool: Renvoie True/False pour dire si les segments peuvent former un triangle
    """
    return True if ( a + b + c > 2*a and a + b + c > 2*b and a + b + c > 2*c ) else False
    
#exo 5
def conversion_masse(poids:float, unite_initiale:str, unite_voulue:str)->float:
    """Fonction pour convertir des unités (ici des masses)

    Args:
        poids (float): variable pour stocker le poids à convertir
        unite_initiale (str): unité de base
        unite_voulue (str): unité voulue

    Returns:
        float: renvoie la valeur du poids convertit
    """
    table=["tonnes","qgrammes","dkgrammes","kilos","hgrammes","dagrammes","grammes","dgrammes","cgrammes","mgrammes"]
    n_initiale = table.index(unite_initiale)
    n_voulue = table.index(unite_voulue)
    puissance = n_voulue - n_initiale
    return poids * 10**puissance

#exo 6
def calculer_mes_impots(mon_revenu:float, nb_adultes:int, nb_enfants:int)->float:
    """Fonction pour calculer ses impots

    Args:
        mon_revenu (int): variable pour stocker son revenu

    Returns:
        float: impots à payer
    """
    quotient_familial = (nb_adultes + 0.5 * nb_enfants)
    apres_premier_cacul = mon_revenu /  quotient_familial
    total_provisoire = 0
    
    if apres_premier_cacul < 11497 : # else pour rajouter les autre if
        total_provisoire = 0
    
    else :
        if apres_premier_cacul > 11497 :
            total_provisoire += ((min(29315, apres_premier_cacul)) - 11498) * 11 / 100
                             
        if apres_premier_cacul > 29315 : 
            total_provisoire += ((min(83823, apres_premier_cacul)) - 29316) * 30 / 100
                             
        if apres_premier_cacul > 83823 :
            total_provisoire += ((min(180294, apres_premier_cacul)) - 83824) * 41 / 100
        
        if apres_premier_cacul > 180294:
            total_provisoire += (apres_premier_cacul - 180295) * 45 / 100
        
    total = total_provisoire * quotient_familial
    
    if total < 3248 and nb_adultes >= 2 :
        return (total - (1470 - (total * 45.25/100)))
    elif total < 1964 and nb_adultes == 1 :
        return (total - (889 - (total * 45.25/100)))
    
    return total
    
    
    
    
    

    