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

def conversion_masse_gpt(poids: float, unite_initiale: str, unite_voulue: str) -> float:
    """
    Convertit un poids d'une unité de masse vers une autre (système métrique).

    Unités supportées : 
        - "tonnes"
        - "qgrammes" (quintaux)
        - "dkgrammes" (décitonnes)
        - "kilos"
        - "hgrammes" (hectogrammes)
        - "dagrammes" (décagrammes)
        - "grammes"
        - "dgrammes" (décigrammes)
        - "cgrammes" (centigrammes)
        - "mgrammes" (milligrammes)

    Args:
        poids (float): valeur à convertir
        unite_initiale (str): unité de départ
        unite_voulue (str): unité d'arrivée

    Returns:
        float: poids converti dans l'unité demandée

    Raises:
        ValueError: si une unité n'est pas reconnue

    Exemple:
        >>> conversion_masse(1, "kilos", "grammes")
        1000.0
        >>> conversion_masse(2500, "grammes", "kilos")
        2.5
    """

    # correspondance en puissances de 10 par rapport au gramme
    puissances = {
        "tonnes": 6,
        "qgrammes": 5,   # quintal (100 kg = 10^5 g)
        "dkgrammes": 4,  # décitonnes (10 kg = 10^4 g)
        "kilos": 3,
        "hgrammes": 2,
        "dagrammes": 1,
        "grammes": 0,
        "dgrammes": -1,
        "cgrammes": -2,
        "mgrammes": -3,
    }

    # normalisation
    unite_initiale = unite_initiale.lower()
    unite_voulue = unite_voulue.lower()

    if unite_initiale not in puissances:
        raise ValueError(f"Unité initiale inconnue : {unite_initiale}")
    if unite_voulue not in puissances:
        raise ValueError(f"Unité voulue inconnue : {unite_voulue}")

    # conversion
    puissance = puissances[unite_voulue] - puissances[unite_initiale]
    return poids * (10 ** puissance)