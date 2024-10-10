import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

turboliste = []

def recursicrap(url):
    try:
        requete = requests.get(url) #, proxies=proxyDict)
        page = requete.content
        soup = BeautifulSoup(page, "lxml")
        liens = soup.find_all('a')
    except:
        return
    if liens:
        for lien in liens:
            if not lien['href'] in turboliste and urlparse(lien['href']).hostname == urlparse(url).hostname:
                turboliste.append(lien['href'])
                print(turboliste)
                recursicrap(lien['href'])
    else:
        turboliste.append(url)

recursicrap("http://172.16.4.12/")
print("------------------")
recursicrap('https://kxs.fr/')
