import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

class DreamScrap:
    def __init__(self, baseurl):
        self.baseurl = baseurl
        self.domaine = urlparse(baseurl).hostname
        self.turboliste = {}
        print(self.baseurl, self.domaine)
        print("-------------------------")

    def one_scrap(self):
        requete = requests.get(self.baseurl)
        page = requete.content
        soup = BeautifulSoup(page, "lxml")
        print(soup.title.string)
        print(requete.status_code)
        liens = soup.find_all('a')
        for lien in liens:
            cible = lien.get('href')
            if urlparse(cible).hostname and urlparse(cible).hostname != self.domaine:
                print("OUT", cible, "-", urlparse(cible).hostname)
            elif cible == "#" or cible == "/":
                print("NULL")
            elif cible != None:
                print("INN", cible)
    
    def multi_scrap(self, link):
        requete = requests.get(link)
        page = requete.content
        soup = BeautifulSoup(page, "lxml")
        print(soup.title.string)
        if requete.status_code == 200:
            liens = soup.find_all('a')
            for lien in liens:
                cible = lien.get('href')
                if self.turboliste[soup.title.string]:
                    if cible != None and cible != "#" and cible != "/":
                        if urlparse(cible).hostname and urlparse(cible).hostname == self.domaine:
                            self.turboliste[soup.title.string] = cible
                            self.multi_scrap(cible)
                        elif not urlparse(cible).hostname:
                            self.turboliste[soup.title.string] = cible
                            self.multi_scrap("https://" + self.domaine + ":/" + cible)
    
    def turbogiver(self):
        print(self.turboliste)


scrapper = DreamScrap("https://f.dreamclouds.fr")
scrapper.multi_scrap("https://f.dreamclouds.fr")
scrapper.turbogiver()