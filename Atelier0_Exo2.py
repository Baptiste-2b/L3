type_lettre = input("Type de lettre (verte / prioritaire / ecopli) : ").lower()
poids = float(input("Poids de la lettre en grammes : "))
sticker = input("Sticker suivi ? (O/N) : ").upper()

prix = 0.0

if type_lettre == "verte":
    if poids <= 20:
        prix = 1.16
    elif poids <= 100:
        prix = 2.32
    elif poids <= 250:
        prix = 4.00
    elif poids <= 500:
        prix = 6.00
    elif poids <= 3000:
        prix = 7.50
    else:
        print("Poids trop élevé pour une lettre verte.")

elif type_lettre == "prioritaire":
    if poids <= 20:
        prix = 1.43
    elif poids <= 100:
        prix = 2.86
    elif poids <= 250:
        prix = 5.26
    elif poids <= 500:
        prix = 7.89
    elif poids <= 3000:
        prix = 10.50
    else:
        print("Poids trop élevé pour une lettre prioritaire.")

elif type_lettre == "ecopli":
    if poids <= 20:
        prix = 1.14
    elif poids <= 100:
        prix = 2.28
    elif poids <= 250:
        prix = 3.92
    else:
        print("Poids trop élevé pour un écopli.")

else:
    print("Type de lettre non reconnu.")

# Ajout du sticker suivi
if sticker == "O":
    prix += 0.50

if prix > 0:
    print(f"Tarif d'affranchissement : {prix:.2f} €")