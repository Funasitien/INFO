from PIL import Image
import PIL
from rich.console import Console
from rich.table import Table
from rich.style import Style
from rich.progress import track
import os
import time

blue_bold = Style(color="blue", blink=True, bold=True)

red_bold = Style(color="red", blink=True, bold=True)

ascii_art = '''                                        
____                    _____ _ _ _           
        |    \ ___ ___ ___ _____|   __|_| | |_ ___ ___ 
         |  |  |  _| -_| .'|     |   __| | |  _| -_|  _|
        |____/|_| |___|__,|_|_|_|__|  |_|_|_| |___|_|  
                                                                                                                
'''

os.system("clear|cls")
console = Console()

# Loader function to generate the pop pop screen
def loader(num=1000):
    # CLear the console
    os.system("clear")
    # Print the ASCII Art bellow
    console.print(ascii_art, justify="center", style="bold cyan")
    # STrange thing to create a timer which change the position of the pops every 0.001 second
    tasks = [f"task {n}" for n in range(1, num)]
    with console.status("[bold cyan]", spinner = 'point') as status:
        while tasks:
            console.print("", justify="center", end="")
            task = tasks.pop(0)
            time.sleep(0.001)
    os.system("clear")

def save(image, name):
    saver = input("Voulez vous sauvegarder votre image ? (O: Oui, N: Non)")
    if saver == "O" or saver == "T" or saver == "0" or saver == "o":
        namer= input("Comment voulez vous appeler le fichier ? (0 Pour le nom par défaut // N'oubliez pas l'extension de fichier)")
        if namer == "O" or namer == "0" or namer == "o":
            image.save(f"filtre-{name}.png")
            print(f"FIchier sauvegarder sous le nom filtre-{name}.png")
        else:
            image.save(namer)
            print(f"FIchier sauvegarder sous le nom {name}")
    else:
        print("Image non sauvegardé")

def redfilter(image):
    for i in range(image.width):
        for j in range(image.height):
            pixel = image.getpixel((i, j))
            image.putpixel((i, j), (pixel[0], 0, 0))
    image.show()
    print("Image filtrer avec le filtre rouge")
    save(image, f"red")

def greenfilter(image):
    for i in range(image.width):
        for j in range(image.height):
            pixel = image.getpixel((i, j))
            image.putpixel((i, j), (0, pixel[1], 0))
    image.show()
    print("Image filtrer avec le filtre vert")
    save(image, f"green")

def bluefilter(image):
    for i in range(image.width):
        for j in range(image.height):
            pixel = image.getpixel((i, j))
            image.putpixel((i, j), (0, 0, pixel[2]))
    image.show()
    print("Image filtrer avec le filtre bleu")
    save(image, f"bleu")         

def grayfilter(image):
    for i in range(image.width):
        for j in range(image.height):
            pixel = image.getpixel((i, j))
            image.putpixel((i, j), (int((pixel[0] + pixel[1] + pixel[2])/3),
                                    int((pixel[0] + pixel[1] + pixel[2])/3),
                                    int((pixel[0] + pixel[1] + pixel[2])/3)))
    image.show()
    print("Image filtrer avec le filtre gris")
    save(image, f"gris")

# Use blackfilter() system but can use color like 255, 0, 255. So it can only show up to 2*2*2 colors.
def saturatefilter(image):
    for i in range(image.width):
        for j in range(image.height):
            pixel = image.getpixel((i, j))
            colorama = ()
            for k, l in enumerate(pixel):
                if l>=128:
                    colorama =  colorama + (255,)
                else:
                    colorama = colorama + (0,)
            image.putpixel((i, j), colorama)
            
    image.show()
    print("Image filtrer avec le filtre saturé")
    save(image, f"saturate")

# Here you can only have 255, 255, 255 or 0, 0, 0 colors
def noirfilter(image):
    for i in range(image.width):
        for j in range(image.height):
            pixel = image.getpixel((i, j))
            if pixel[0] + pixel[1] + pixel[2] >= 383:
                image.putpixel((i, j), (255, 255, 255))
            else:
                image.putpixel((i, j), (0, 0, 0))
            
    image.show()
    print("Image filtrer avec le filtre noir")
    save(image, f"noir")

# Mirroring pixel on X axis
def miroirfilter(image):
    render = Image.new("RGB", (image.width, image.height))
    for i in range(image.width):
        for j in range(image.height):
            pixel = image.getpixel((i, j))
            render.putpixel((image.width - i - 1, j), pixel)
    render.show()
    print("Image filtrer avec le filtre Mirroir") 
    save(image, f"mirroir")
            
# Mirroring pixel on Y axis
def reversefilter(image):
    render = Image.new("RGB", (image.width, image.height))
    for i in range(image.width):
        for j in range(image.height):
            pixel = image.getpixel((i, j))
            render.putpixel((i, image.height - j - 1), pixel)
            
    render.show()
    print("Image filtrer avec le filtre Reverse")
    save(image, f"revserse")

# Here come the big boy:
# The pixel filter, to rasterise images
def pixelfilter(image, n):
    # Create a loop but instead of doing each pixel, we do n * rasterise pixel. Allow us to change the resolution with n
    for i in range(0, image.width - n, n):
        for j in range(0, image.height, n):
            pixelist = []
            for k in range(n):
                for l in range(n):
                    # Add all the pixel of the square of n lenth to a list called pixelist
                    pixelist.append(image.getpixel((i+k, j+l)))
            
            # Then we take each first value of every tupple in the pixelist        
            pe1 = [tup[0] for tup in pixelist]
            # Sum is the addition of every item in pe1, and n*n is the square of n, so the pixel defnition
            px1 = sum(pe1) / (n*n)
            # Same for second value
            pe2 = [tup[1] for tup in pixelist]
            px2 = sum(pe2) / (n*n)
            # And first value
            pe3 = [tup[2] for tup in pixelist]
            px3 = sum(pe3) / (n*n)                    
                                 
            # Then we write each pixel with the same color in the big pixel of size n                       
            for m in range (n):
                for o in range (n):
                    image.putpixel((i+m, j+o), (int(px1), int(px2), int(px3)))
        
    image.show()
    print("Image filtrer avec le filtre pixel", n)
    save(image, f"pixel-{n}")            

def lumfilter(image, x):
    for i in range(image.width):
        for j in range(image.height):
            pixel = image.getpixel((i, j))
            image.putpixel((i, j), (pixel[0] + x, pixel[1] + x, pixel[2] + x))
    image.show()
    print("Image filtrer avec le filtre Luminosité", x)
    save(image, f"luminosité-{x}")

def retrofilter(image, n):
    for i in range(image.width):
        for j in range(image.height):
            pixel = image.getpixel((i, j))
            image.putpixel((i, j), ((int(pixel[0]/n)*n), (int(pixel[1]/n)*n), (int(pixel[2]/n)*n)))
            
    image.show()
    save(image, "rétro")

def select():
    console.print(ascii_art, justify="center", style="bold cyan")
    console.print("Quel fichier voulez vous ouvrir ? ", justify="center", style=blue_bold)
    console.print("(1 pour le fichier par défaut)", justify="center", style=blue_bold)
    value = str(input("? "))
    if value == "1":
        return "maison.jpg"
    else:
        return value

def menu():
    console.print(ascii_art, justify="center", style="bold cyan")
    console.print("Quel filtre voulez vous appliquer à votre image ? ", justify="center", style=blue_bold)
    console.print("1 - Filtre Rouge", justify="center", style=blue_bold)
    console.print("2 - Filtre Bleu", justify="center", style=blue_bold)
    console.print("3 - Filtre Vert", justify="center", style=blue_bold)
    console.print("4 - Filtre Gris", justify="center", style=blue_bold)
    console.print("5 - Filtre Noir", justify="center", style=blue_bold)
    console.print("6 - Filtre Saturé", justify="center", style=blue_bold)
    console.print("7 - Filtre Retro", justify="center", style=blue_bold)
    console.print("8 - Filtre Mirroir", justify="center", style=blue_bold)
    console.print("9 - Filtre Luminosité + 10", justify="center", style=blue_bold)
    console.print("10 - Filtre Luminosité + 50", justify="center", style=blue_bold)
    console.print("11 - Filtre Pixel3", justify="center", style=blue_bold)
    console.print("12 - Filtre Pixel10", justify="center", style=blue_bold)
    console.print("13 - Filtre Reverse", justify="center", style=blue_bold)
    console.print("14 - Filtre Retro Super", justify="center", style=blue_bold)
    console.print("15 - Filtre Retro Super Mega ++", justify="center", style=blue_bold) 
    
    console.print("", justify="center", style=blue_bold) 
    console.print("0 - Quitter", justify="center", style=red_bold) 
    
def loop(image):
    filtre = int(input("? "))
    if filtre == 1:
        redfilter(image)
    elif filtre == 2:
        bluefilter(image)
    elif filtre == 3:
        greenfilter(image)
    elif filtre == 4:
        grayfilter(image)
    elif filtre == 5:
        noirfilter(image)
    elif filtre == 6:
        saturatefilter(image)
    elif filtre == 7:
        retrofilter(image, 32)
    elif filtre == 8:
        miroirfilter(image)
    elif filtre == 9:
        lumfilter(image, 10)
    elif filtre == 10:
        lumfilter(image, 50)
    elif filtre == 11:
        pixelfilter(image, 3)
    elif filtre == 12:
        pixelfilter(image, 10)
    elif filtre == 13:
        reversefilter(image)
    elif filtre == 14:
        retrofilter(image, 64)
    elif filtre == 15:
        retrofilter(image, 128)
    elif filtre == 0:
        print("Au Revoir :D")
        return "break"
    else:
        print("Ce filtre n'existe pas :c")
        
# The loader function clear the console and show the loading screen
loader()
# Function to choose a file
file = select()
loader(300)
menu()
source = Image.open(file)
try:
    while True:
        # Loop is the "choice" function
        test = loop(source)
        if test == "break":
            break
        source = Image.open(file)

except KeyboardInterrupt:
    print("Au revoir :)")