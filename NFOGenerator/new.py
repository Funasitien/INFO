from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from dreamlogger import *
from os import walk
from os.path import exists
from math import floor

# Activation de quelques infos dans la console avec ma super extension
debug_mode(True)
clear()


#Petite non-fonction qui cherche tout les fichiers présent
files = []
for (dirpath, dirnames, filenames) in walk("."):
    for file in filenames:
        files.append(dirpath+"/"+file)
# Et qui les tries
files.sort()


# Fonction principal qui Génère le fichier nfo
def nfo(file):
    deleted = False
    # Initialize d'abbord les variables
    totalminutes = 0
    totalsecondes = 0
    totalsize = 0
    # Puids fait une boucle pour chaque fichier récupéré dans la boucle précédente
    for songs in file:
        if songs.endswith('.mp3'):
            debug(songs)
            infos = ID3(songs)
            texte = ""
            titre = infos["TALB"].text[0]
            
            """
            Ici, un grand nombre de fonction va essayer de récupérer le plus de données sur le fichier mp3
            Et contrairement à votre code, ne va pas mourrir si il y a une erreur
            Le titre et la fonction de chque boucle est écrit au dessus
            """
            
            # Titre de la piste
            try:
                titre = infos["TALB"].text[0]
                info(f"Album : {titre}")
                # Artiste
                try:
                    artiste = infos['TPE1'].text[0]
                    info(f"Artiste : {artiste}")
                except:
                    artiste = "Unknow"
                    error("Aucun artiste trouvé")          
                
                # Création du fichier nfo, mais en .max car max c'est mieux
                file_exists = exists(f"{titre}.max")
                # Si le fichier existe, il écrit le titre de l'artiste
                if file_exists != True:
                
                    file = open(f"{titre}.max", "w")
                    title = center_text(f'{artiste} - {titre}')
                    file.write(f'----------------------------------------------------------------------\n{title}\n----------------------------------------------------------------------\n\n')
                    file.write(f'Artist..............: {artiste}\n')
                
                    # Puis récupère les informations global de l'album 1 fois
                    # Nom de l'album
                    try:
                        album = infos["TALB"].text[0]
                        info(f"Album : {album}")
                        file.write(f"Album...............: {album}", "w")
                        
                    except:
                        error("Aucun num trouvé")
                    
                    
                    # Genre de l'album
                    try:
                        genre = infos["TCON"].text[0]
                        info(f"Genre : {genre}")
                        file.write(f'Genre...............: {genre}\n')
                    except:
                        error("Aucun genre trouvé")
                        
                    # Année de sortietitre = infos["TALB"].text[0]
                    try:
                        year = infos["TDRC"].text[0]
                        info(f"Année : {year}")
                        file.write(f'Year................: {year}\n')
                    except:
                        error("Aucune date trouvé")


                    audio = MP3(songs)
                    # Longugeur en secondes de la piste
                    length = audio.info.length
                    # Le nombre de channels audio
                    file.write(f'Channels............: {audio.info.channels}\n')
                    # Le débit (bitrate) en bits par seconde
                    file.write(f'Quality.............: {round(audio.info.bitrate / 1000)} kbps\n')
                    # Le sampling rate (fréquence d'échantillonnage) en Hz
                    file.write(f'Sampling rate.......: {audio.info.sample_rate / 1000} kHz\n')
                    # Le bitrate mode (on ne l'utilisera pas ici)
                    file.write('Format..............: MPEG Audio Layer 3 (MP3)\n')
                    if exists("cover.jpg"):
                        file.write('Cover...............: Front\n')
                    # Le ripper (extracteur) utilisé
                    file.write(f'Ripper..............: {audio.info.encoder_info}\n')
                    # Le mode (0 : Stereo ; 1 : Joint stereo ; 2 : Dual channel ; 3 : Mono)
                    mode = audio.info.mode
                    if mode == 0:
                        file.write('Mode................: Stereo\n')
                    elif mode == 1:
                        file.write('Mode................: Joint-Stereo\n')
                    elif mode == 2:
                        file.write('Mode................: Dual-Channel\n')
                    elif mode == 3:
                        file.write('Mode................: Mono\n')
                
                # Continue ensuite avec la tracklist
                # Nouméro de la piste
                audio = MP3(songs)
                length = audio.info.length
                
                try:
                    numero = infos["TRCK"].text[0]
                    info(f"Numéro : {numero}")
                    if len(numero) == 1:
                        numero = f"0{numero}"
                    
                except:
                    error("Aucun numéro trouvé")
                    numero = "0X"
                
                
                try:
                    name = infos["TIT2"].text[0]
                    info(f"Titre : {name}")
                    
                except:
                    error("Aucun Titre trouvé")
                    name = "Inconu RIP"
                
                texte = f'{numero}. {artiste} - {name}'
                
                file.write('\n\n----------------------------------------------------------------------\n                             Tracklisting\n----------------------------------------------------------------------\n\n')
                file.close()
                print()
                
            except:
                error("Aucun titre trouvé")
            
            # Sort de la boucle pour générer les informations globale
            
            minutes = round(length) // 60
            secondes = round(length)%60
            
            if minutes < 10:
                minutes = f"0{minutes}"
                
            if secondes < 10:
                secondes = f"0{secondes}"
                
            for j in range(1, 61 - len(texte)):
                texte = texte + " "
                
            filee = open(f"{titre}.max", "a")
            filee.write(f"   {texte}[{minutes}:{secondes}]\n")
            
            totalminutes = int(totalminutes) + int(minutes)
            totalsecondes = int(totalsecondes) + int(secondes)
            totalsize = totalsize + os.path.getsize(songs)
    
    totalminutes = totalminutes + round(totalsecondes) // 60
    totalsecondes = round(totalsecondes)%60

    filee.write(f"\nPlaying time........: {totalminutes}:{totalsecondes}\n")   
    filee.write(f"Total size..........: {round(totalsize / 1024 / 1024)}Mb\n")

    
# Fonction qui centre le titre    
def center_text(text):
    trucbequistant = int(len(text)/2)
    spaceing = ""
    for i in range(1, 35 - trucbequistant):
        spaceing = spaceing + " "
        
    return spaceing + text


nfo(files)