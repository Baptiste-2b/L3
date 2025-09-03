import random

# Choix possibles
CHOIX = ["pierre", "papier", "ciseaux", "puits"]

# Demande si on joue contre la machine ou non
contre_machine = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ").upper()
if contre_machine not in ['O', 'N']:
    print("Je n'ai pas compris votre réponse")
    exit()

if contre_machine == 'O':
    nom_joueur1 = input("Quel est votre nom ? ")
    print("Bienvenue", nom_joueur1, "nous allons jouer ensemble \n")
    nom_joueur2 = 'Machine'
else:
    nom_joueur1 = input("Quel est votre nom ? ")
    nom_joueur2 = input("Quel est le nom du deuxième joueur ? ")
    print("Bienvenue", nom_joueur1, "et", nom_joueur2, "nous allons jouer ensemble \n")

# Initialisation des scores et du compteur
score_joueur1, score_joueur2, manche = 0, 0, 0
continuer = True

while continuer:
    manche += 1

    # Choix du joueur 1
    choix_joueur1 = input(f"{nom_joueur1}, faites votre choix parmi {CHOIX} : ").lower()
    while choix_joueur1 not in CHOIX:
        print("Je n'ai pas compris votre réponse")
        choix_joueur1 = input(f"{nom_joueur1}, faites votre choix parmi {CHOIX} : ").lower()

    # Choix du joueur 2
    if nom_joueur2 == "Machine":
        choix_joueur2 = random.choice(CHOIX)
    else:
        choix_joueur2 = input(f"{nom_joueur2}, faites votre choix parmi {CHOIX} : ").lower()
        while choix_joueur2 not in CHOIX:
            print("Je n'ai pas compris votre réponse")
            choix_joueur2 = input(f"{nom_joueur2}, faites votre choix parmi {CHOIX} : ").lower()

    # On affiche les choix
    print("Si on récapitule :", nom_joueur1, choix_joueur1, "et", nom_joueur2, choix_joueur2, "\n")

    # Détermination du gagnant
    if choix_joueur1 == choix_joueur2:
        print("Égalité cette manche")
    elif (choix_joueur1 == "pierre" and choix_joueur2 == "ciseaux") or \
         (choix_joueur1 == "papier" and choix_joueur2 in ["pierre", "puits"]) or \
         (choix_joueur1 == "ciseaux" and choix_joueur2 == "papier") or \
         (choix_joueur1 == "puits" and choix_joueur2 in ["pierre", "ciseaux"]):
        score_joueur1 += 1
        print("Le gagnant est", nom_joueur1)
    else:
        score_joueur2 += 1
        print("Le gagnant est", nom_joueur2)

    print(f"Scores : {nom_joueur1} = {score_joueur1} | {nom_joueur2} = {score_joueur2}\n")

    # Arrêt au bout de 5 manches
    if manche == 5:
        continuer = False
    else:
        go = input(f"Souhaitez-vous refaire une partie {nom_joueur1} contre {nom_joueur2} ? (O/N) ").upper()
        if go == 'N':
            continuer = False
        elif go != 'O':
            print("Réponse invalide, on continue...")

print("Merci d'avoir joué ! À bientôt ")
