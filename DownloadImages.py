#!/usr/bin/python3
#-*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
def download_google(word, nbPic):
    url = 'https://www.google.com/search?q=' + word + '&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    i = 0
    for raw_img in soup.find_all('img'):
    	if(i < nbPic):
    		link = raw_img.get('src')
    		os.system("wget " + link)
    		i = i+1
    	else:
    		break

if __name__ == '__main__':
    #word = input("Input key word: ")
    #download_baidu(word)
    arr = ["zorro", "pain", "oeufs", "bois", "platre", "zinc", "saucisse", "chaussette", "huitre", "oeuf", "disque", "bronze", "toulouse", "trésor", "oeuil", "samu", "mamie", "désinsectisant", "pompiers", "corde à noeuds", "vin", "sortie de secours", "flics", "ventre", "vercingétorix", "sapin de noel", "autoroute", "petite vis fraisée", "tonneau de vin qui fuit", "père", "train", "livre de maths", "mine d'or", "maman", "soeure", "diable", "mage", "mecque", "mauve", "plan", "une rose", "rateau", "reine", "rame", "rire", "rouleau", "sang", "boitier DVD", "rive", "une rappe", "une laisse", "latte sommier", "pelotte de laine", "couteau", "une lire", "une aile d'avion", "luge", "un lac", "lave", "lapin", "chaise", "chateau", "un chene", "chameau", "charrue", "un chale marron", "un juge", "un cheque", "chauve", "chapeau", "une case africaine", "gâteau", "une canne", "camion", "un carré", "calin", "une cage", "caca", "café", "une cape rouge", "un vase", "pantalon", "veine", "Kim kardashian", "un phare", "foule", "juif", "une faque", "un fauve", "sarkozy", "un pouce", "des pates", "panier", "paume de main", "tour eiffel", "une poule", "une pioche", "une pique chevalier", "graine de pavot"]
    #print(len(arr))
    for im in arr:
    	download_google(im, 1)