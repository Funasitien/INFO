from rich.console import Console
from rich.table import Table
from rich.style import Style
from rich.progress import track
import os
import time
import sqlite3


green_bold = Style(color="blue", blink=True, bold=True)

ascii_art = '''
-     ___            _             _                   -
-    / __\___  _ __ | |_ __ _  ___| |_     _     _     -
-   / /  / _ \| '_ \| __/ _` |/ __| __|  _| |_ _| |_   -
-  / /__| (_) | | | | || (_| | (__| |_  |_   _|_   _|  -
-  \____/\___/|_| |_|\__\__,_|\___|\__|   |_|   |_|    -                          
'''

os.system("clear")
open("fichier.txt", "a")
link_list = []
console = Console()

"""
Initialize la base de donné une fois par execution
"""
conn = sqlite3.connect('./data.db', timeout=10)
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, mail TEXT, telephone INTEGER, adresse TEXT, date TEXT)')
cur.close()

def loader(num=1000):
    """
    Fonction illisible qui génère le spinner.
    """
    os.system("clear")
    console.print(ascii_art, justify="center", style="bold blue")
    tasks = [f"task {n}" for n in range(1, num)]
    with console.status("[bold blue]", spinner = 'point') as status:
        while tasks:
            console.print("", justify="center", end="")
            task = tasks.pop(0)
            time.sleep(0.001)
    os.system("clear")

class Menu:
    
    """
    Classe princpal de l'application

    Enfants :
    - create() qui permet d'ajouter un contact
    - delete() qui permet de supprimer un contact
    - show() qui affiche tout les contacts
    - search() qi fonctionne comme show mais avec un argument
    """

    def __init__(self, data=None):
        os.system("clear")
        console.print(ascii_art, justify="center", style="bold cyan")
        if data:
            console.print(data, justify="center", style=green_bold)
        
        console.print('''
Que voulez-vous faire ?
1 - Ajouter un contact
2 - Supprimmer un contact
3 - Afficher tous les contacts
4 - Chercher un contact
5 - Quitter
''', justify="center")
        
        print()
        a = input("Choix: ? ")
    
        if a == "1":
            Menu.create()
        
        if a == "2":
            Menu.delete()
        
        if a == "3":
            Menu.show()
            
        if a == "4":
            Menu.search()
        
        if a == "6":
            Menu.file_import()
    
        if a == "5":
            console.print("Au revoir !", justify="center", style="#D3869B bold")
            quit()
        else:
            Menu()
            
    def create(self=None):
        """
        Fonction qui permet de créer un contacts
        Arguments: déclarés par inputs
        """
        prenom = input("Prénom de votre contact : ")
        nom = input("Nom de votre contact : ")
        mail = input("Mail de votre contact : ")
        telephone = input("Téléphone de votre contact : ")
        adresse = input("Adresse de votre contact : ")
        date = input("Date de naissance de votre contact : ")
        cur = conn.cursor()
        cur.execute("INSERT INTO contacts(prenom, nom, mail, telephone, adresse, date) VALUES (?, ?, ?, ?, ?, ?)", (prenom, nom, mail, telephone, adresse, date))
        cur.close()
        
        Menu("Contact Créé !")

    def delete(self=None):
        """
        Fonction qui permet de supprimer un ou plusieurs contacts
        Arguments: déclarés par inputs
        """
        delete_input = input("Nom du contact que vous voulez supprimer ? : ")
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute('SELECT * FROM contacts WHERE prenom = ? OR nom = ? OR mail = ? OR telephone = ? OR adresse = ? OR date = ?', (delete_input, delete_input, delete_input, delete_input, delete_input, delete_input))
        lignes = cur.fetchall()
        for line in lignes:
            if delete in line:
                a = input("Voulez vous supprimler le contact " + line[0] + "? [y/n]")
                if a:
                    if a == "y":
                        cur.execute('DELETE FROM contacts WHERE prenom = ?', (line[0],))
        cur.close()
        Menu()


    def search(self=None):
        """
        Permet de chercher un string dans toute la base de fichier
        Argument : déclaré pr l'input'
        """
        
        search_input = input("Donné sur contact que vous voulez chercher (Nom, Mail...) : ")
        
        stable = Table(show_header=True, header_style="bold cyan", expand=True)
        stable.add_column("Prénom", style="dim", width=15, justify="center")
        stable.add_column("Nom", style="dim", width=15, justify="center")
        stable.add_column("Mail", style="dim", width=30, justify="center")
        stable.add_column("Téléphone", style="dim", width=20, justify="center")
        stable.add_column("Date de Naissance", style="dim", width=16, justify="center")
        
        cur = conn.cursor()
        cur.execute('SELECT * FROM contacts WHERE prenom = ? OR nom = ? OR mail = ? OR telephone = ? OR adresse = ? OR date = ?', (search_input, search_input, search_input, search_input, search_input, search_input))
        lignes = cur.fetchall()
        cur.close()
        for line in lignes:
            stable.add_row(
                str(line[1]),
                str(line[2]),
                str(line[3]),
                str(line[4]),
                str(line[6])
            )
        
        loader(300)
        console.print(ascii_art, justify="center", style="bold cyan")
        console.print(stable, justify="center")
        print()
        a = input("")
        Menu()

    

    def show(self=None):
        """
        Permet de chercher un string dans toute la base de fichier
        Argument : Type de recherche déclaré par input'
        """
        
        search_filter = int(input("  Sélétctionnez un filtre pour modifier l'odre des contacts "))
        # Génère un tableau RICH
        table = Table(show_header=True, header_style="bold cyan", expand=True)
        table.add_column("Prénom", style="dim", width=15, justify="center")
        table.add_column("Nom", style="dim", width=15, justify="center")
        table.add_column("Mail", style="dim", width=30, justify="center")
        table.add_column("Téléphone", style="dim", width=20, justify="center")
        table.add_column("Date de Naissance", style="dim", width=16, justify="center")

        cur = conn.cursor()
        cur.execute(f'SELECT * FROM contacts')
        lignes = cur.fetchall()
        cur.close()

        unfolded = []
        for data in lignes:
            unfolded.append((data[1],data[2],data[3],data[4],data[6]))

        # Trie celon la première lettre de l'élément x du tupple
        if search_filter == 1:
            unfolded = sorted(unfolded, key=lambda x: x[0].lower())
        elif search_filter == 2:
            unfolded = sorted(unfolded, key=lambda x: x[1].lower())

        for line in unfolded:
            table.add_row(
                str(line[0]),
                str(line[1]),
                str(line[2]),
                str(line[3]),
                str(line[4])
            )
    
        loader(300)
        console.print(ascii_art, justify="center", style="bold cyan")
        console.print(table, justify="center")
        print()
        a = input("")
        Menu()
    
    def file_import(self=None):
        f = open("fichier.txt", "r") # Ouvre en lecture le fichier
        for line in f:
            data = line.split(":")
            cur = conn.cursor()
            cur.execute("INSERT INTO contacts(prenom, nom, mail, telephone, adresse, date) VALUES (?, ?, ?, ?, ?, ?)", (data[0],data[1],data[2],data[3],data[4],data[5],))
            cur.close()
    
loader()
Menu()
