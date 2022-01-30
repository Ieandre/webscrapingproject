# -*- coding: utf-8 -*-
"""WebScrappingProject

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O3ENPTjdIDGe_zyS6nzX6E2pxeNMt4E3

# Installation des librairies demandées
"""

pip install beautifulsoup4

import urllib.request
import csv
from bs4 import BeautifulSoup
f = open("test.csv", "w", newline="")
writer = csv.writer(f)
soup = BeautifulSoup(urllib.request.urlopen('https://www.zonebourse.com/cours/action/ORANGE-4649/fondamentaux/'), 'lxml')

tableau1 = soup('table', {"class" : "BordCollapseYear2"})[0]
tableau2 = soup('table', {"class" : "BordCollapseYear2"})[1]



capitalisation = tableau1.findAll('tr')[5].get_text(" ")
print(capitalisation)


per = tableau1.findAll('tr')[3].get_text(" ")
print(per)


bna = tableau2.findAll('tr')[8].get_text(" ")
print(bna)