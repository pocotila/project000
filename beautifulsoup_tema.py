# Pe siteul https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/
# sunt trecute zilnic numarul de date raportat la nivel de judet.
# URLul utilizat este compus, in cea mai mare parte a requesturi din periaoda 3 aprilie - 24 aprilie
# din https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/ ,
# deci requesturile se pot automatiza. In cazul in care nu se gasesc date la requestul dorit intr-o zi
# (mai exista si exceptii in care urlul este format altfel, vezi 1 si 2 aprilie), nu se vor trece date.
#  Se doreste realizarea unui tabel comun pe judete pentru ultimele 7 zile de la data 20.01.
# Se exporta datele in Excel.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

url = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/'

def get_table(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    tablelist = []
    table = soup.find('table, class = ')
# print(r.text)




