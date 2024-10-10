import os
from rich.console import Console
from rich.table import Table
from rich.style import Style

console = Console()

ascii_art = '''                                        
 _____     _                            ___ 
|  _  |_ _|_|___ ___ ___ ___ ___ ___   | | |
|   __| | | |_ -|_ -| .'|   |  _| -_|  |_  |
|__|  |___|_|___|___|__,|_|_|___|___|    |_|                                              
'''


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class color:
    g = '\033[92m' # vert
    y = '\033[93m' # jaune
    r = '\033[91m' # rouge
    b = '\033[34m' # Bleu
    n = '\033[0m' #gris, couleur normale 97 107
    w = '\033[97m'

jeu = ([0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0]
      )


def affiche_grille(tab):
    cls()
    w = 0
    console.print(ascii_art, justify="center", style="red bold")
    console.print(' ⭐️  🗿️  ⭐️  🗿️  ⭐️  🗿️  ⭐️ ', justify="center")
    print('')
    console.print('┌────┬────┬────┬────┬────┬────┬────┐', justify="center")
    for table in tab:
        w = w + 1
        ligne = f"│"
        for child in table:
            if child == 0:
                ligne = ligne + "    "
            if child == 1:
                ligne = ligne + " ⭐️ "
            if child == 2:
                ligne = ligne + " 🗿️ "
            ligne = ligne + "│"
        console.print(ligne, justify="center")
        if w == 6:
            console.print('└────┴────┴────┴────┴────┴────┴────┘', justify="center")
            console.print('0️⃣    1️⃣    2️⃣    3️⃣    4️⃣    5️⃣    6️⃣   ', justify="center")
            print('')
        else:
            console.print('├────┼────┼────┼────┼────┼────┼────┤', justify="center")


def colonne_libre(tab, colonne):
    test = tab[0]
    if test[colonne] != 0:
        return False
    else:
        return True
    

def place_jeton(tab, colonne, joueur):
    colonne = colonne
    game = tab[::-1]
    for i, table in enumerate(game):
        if table[colonne] == 0:  
            tab[5-i][colonne] = joueur
            break
            
    return tab

# Fonction de jeu pour le joueur "joueur"
def tour_joueur(tab, joueur):
    # Demande un chiffre et recommence si ce n'est pas un chiffre
    try:
        ask = int(console.input("Dans quelle colonne voulez vous mettre votre pion ? "))
    except:
        print("Je te demande un chiffre. Pas une intégralle.")
        tour_joueur(tab, joueur)
    
    # Teste le jeton
    try:
        # Teste des erreurs pottentiels de spam
        if ask or ask==0:
            test = colonne_libre(tab, ask)
        else:
            console.print(f"Une erreur est survenu. Utilise le programme normalement s'il te plait. Et arrète de détruire ton clavier. {ask}",  style="red bold")

    # Vérifie si on peux placer un jeton dans la position demander
    except:
        print("Vous ne pouvez pas jouer de jeton ici !")
        tour_joueur(tab, joueur)    

    # Place le jeton si le test est positif
    if test  == True:
        place_jeton(tab, ask, joueur)
        affiche_grille(tab)
    
    # Ou renvoi une erreur si c'est pas possible
    else:
        print("Vous ne pouvez pas jouer de jeton ici !")
        tour_joueur(tab, joueur)
        
# Vérifie horizontalement dans la grille si un piont est gagnant
def horizontale(tab, joueur):
    for line in tab:
        won = 0
        for child in line:
            if child == joueur:
               won = won + 1
            else:
                won = 0
                
            if won == 4:
                return True
    return False

# Vérifie verticalement dans la grille si un piont est gagnant
def verticale(tab, joueur):
    for num in range(7): # taille de tab.line
        for line in tab:
            if line[num] == joueur:
                won = won + 1
            else:
                won = 0
                
            if won == 4:
                return True
    return False

# Vérifie diagonalement de haut en bas par la droite si on piont est gagnant
def diag_right(tab, joueur):
    for i in range(3):
        for j in range(4):
            won = 0
            for k in range(4):
                # print(i, j, k)
                if tab[i + k][j + k] == joueur:
                    won = won + 1
                else:
                    won = 0
                if won == 4:
                    return True
    return False

# Vérifie diagonalement de haut en bas par la gauche si on piont est gagnant
def diag_left(tab, joueur):
    for i in range(3):
        for j in range(3, 7):
            won = 0
            for k in range(4):
                #print(i, j, k)
                if tab[i + k][j - k] == joueur:
                    won = won + 1
                else:
                    won = 0
                if won == 4:
                    return True
    return False


# Vérifie si un pion est gagnant et returne True si oui (grace au OR)
def gagne(tab, joueur):
    return horizontale(tab, joueur) or verticale(tab, joueur) or diag_right(tab, joueur) or diag_left(tab, joueur)


# Lance la partie
win = False

while win == False:
    # In range joueur 1 joueur 2
    for i in range (1, 3):
        affiche_grille(jeu)
        if i == 1:
            console.print("Joueur ⭐️", justify="center")
        else:
            console.print("Joueur 🗿️", justify="center")
        tour_joueur(jeu, i)
        if gagne(jeu, i) == True:
            console.print(f"Le joueur {i} a gagné !!!!!", style="cyan bold")
            win = True
            break
