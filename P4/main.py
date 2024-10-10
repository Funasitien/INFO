from rich.console import Console
from rich.table import Table
from rich.style import Style
from rich.progress import track
import os
import time

green_bold = Style(color="green", blink=True, bold=True)

ascii_art = '''
___            _             _        
      / __\___  _ __ | |_ __ _  ___| |_    _   
       / /  / _ \| '_ \| __/ _` |/ __| __|  | |_ 
        / /__| (_) | | | | || (_| | (__| |  |_   _|
     \____/\___/|_| |_|\__\__,_|\___|\__|  |_|  
                                                                  
'''


os.system("clear")
open("fichier.txt", "a")
link_list = []
console = Console()


def loader(num=1000):
    os.system("clear")
    console.print(ascii_art, justify="center", style="bold cyan")
    tasks = [f"task {n}" for n in range(1, num)]
    with console.status("[bold cyan]", spinner = 'point') as status:
        while tasks:
            console.print("", justify="center", end="")
            task = tasks.pop(0)
            time.sleep(0.001)
    os.system("clear")

class Menu:
    
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
    
        if a == "5":
            console.print("Au revoir !", justify="center", style="#D3869B bold")
            quit()
        else:
            Menu()
            
    def create(self=None):
        prenom = input("Prénom de votre contact : ")
        nom = input("Nom de votre contact : ")
        mail = input("Mail de votre contact : ")
        telephone = input("Téléphone de votre contact : ")
        adresse = input("Adresse de votre contact : ")
        date = input("Date de naissance de votre contact : ")
        f = open("fichier.txt", "a")
        f.write(prenom+":"+nom+":"+mail+":"+telephone+":"+adresse+":"+date+"\n")
        f.close()
        Menu("Contact Créé !")

    def delete(self=None):
        delete = input("Donné sur contact que vous voulez supprimer (Nom, Mail...) : ")
        print(delete)

        with open("fichier.txt", "r") as fp:
            lines = fp.readlines()

        with open("fichier.txt", "w") as fp:
            for line in lines:
                if delete in line:
                    a = input("Voulez vous supprimler le contact " + line.replace(":" , " ") + "? [y/n]")
                    if a:
                        if a == "y":
                            pass
                        else:
                            fp.write(line)
                    else:
                        fp.write(line)
                else:
                    fp.write(line)
        Menu()


    def search(self=None):
        delete = input("Donné sur contact que vous voulez chercher (Nom, Mail...) : ")
        
        stable = Table(show_header=True, header_style="bold cyan", expand=True)
        stable.add_column("Prénom", style="dim", width=15, justify="center")
        stable.add_column("Nom", style="dim", width=15, justify="center")
        stable.add_column("Mail", style="dim", width=30, justify="center")
        stable.add_column("Téléphone", style="dim", width=20, justify="center")
        stable.add_column("Date de Naissance", style="dim", width=16, justify="center")
        
        f = open("fichier.txt", "r")
        for line in f:
            if delete in line:
                data = line.split(":")
                stable.add_row(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[5],
                )
        loader(300)
        console.print(ascii_art, justify="center", style="bold cyan")
        console.print(stable, justify="center")
        print()
        a = input("")
        Menu()

    

    def show(self=None):
        table = Table(show_header=True, header_style="bold cyan", expand=True)
        table.add_column("Prénom", style="dim", width=15, justify="center")
        table.add_column("Nom", style="dim", width=15, justify="center")
        table.add_column("Mail", style="dim", width=30, justify="center")
        table.add_column("Téléphone", style="dim", width=20, justify="center")
        table.add_column("Date de Naissance", style="dim", width=16, justify="center")

        f = open("fichier.txt", "r") # Ouvre en lecture le fichier
        for line in f: # Parcourt toute les lignes
            data = line.split(":")

            table.add_row(
                data[0],
                data[1],
                data[2],
                data[3],
                data[5],
            )
    
        loader(300)
        console.print(ascii_art, justify="center", style="bold cyan")
        console.print(table, justify="center")
        print()
        a = input("")
        Menu()
    
    
loader()
Menu()