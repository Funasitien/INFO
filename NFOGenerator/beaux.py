from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from dreamlogger import *
from os import walk


debug_mode(False)
clear()

files = []
for (dirpath, dirnames, filenames) in walk("."):
    for file in filenames:
        files.append(dirpath+"/"+file)

files.sort()
    
def nfo(songs):
    if songs.endswith('.mp3'):
        debug(songs)
        infos = ID3(songs)
            
        # Titre de la piste
        try:
            titre = infos["TIT2"].text[0]
            info(f"Titre : {titre}")
            try:
                artiste = infos['TPE1'].text[0]
                info(f"Artiste : {artiste}")
            except:
                artiste = "Unknow"
                error("Aucun artiste trouvé")
            
            file = open(f"{titre}.max", "w")

            title = center_text(f'{artiste} - {titre}')
                
            file.write(f'----------------------------------------------------------------------\n{title}\n----------------------------------------------------------------------\n\n')
            file.write(f'Artist..............: {artiste}\n')
             
        except:
            error("Aucun titre trouvé")
            
        # Nom de l'album
        try:
            album = infos["TALB"].text[0]
            info(f"Album : {album}")
            file.write(f'Album...............: {album}\n')
        except:
            error("Aucun album trouvé")
        
        # Numero de la pistes
        try:
            numero = infos["TRCK"].text[0]
            info(f"Numéro : {numero}")
            file.write(f'N°..................: {numero}\n')
        except:
            error("Aucun num trouvé")
        # Nom de l'artiste ou du goupe
        
        # Genre de l'album
        try:
            genre = infos["TCON"].text[0]
            info(f"Genre : {genre}")
            file.write(f'Genre...............: {genre}\n')
        except:
            error("Aucun genre trouvé")
            
        # Année de sortie
        try:
            year = info["TDRC"].text[0]
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
        file.write(f'Sampling rate.......: {audio.info.sample_rate} Hz\n')
        # Le bitrate mode (on ne l'utilisera pas ici)
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
           
        file.close()
        print()

def center_text(text):
    trucbequistant = int(len(text)/2)
    spaceing = ""
    for i in range(1, trucbequistant):
        spaceing = spaceing + " "
        
    return spaceing + text

for song in files:
    nfo(song)