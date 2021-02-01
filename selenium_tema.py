# Pe siteul https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/
# sunt trecute zilnic numarul de date raportat la nivel de judet.
# URLul utilizat este compus, in cea mai mare parte a requesturi din periaoda 3 aprilie - 24 aprilie
# din https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/ ,
# deci requesturile se pot automatiza. In cazul in care nu se gasesc date la requestul dorit intr-o zi
# (mai exista si exceptii in care urlul este format altfel, vezi 1 si 2 aprilie), nu se vor trece date.
#  Se doreste realizarea unui tabel comun pe judete pentru ultimele 7 zile de la data 20.01.
# Se exporta datele in Excel.


from selenium import webdriver

import pandas as pd

driver = webdriver.Chrome(executable_path="C:\Chrome\chromedriver.exe")

ziua = "21"
# zile = [21, 22, 23, 24, 25, 26, 27]
#
# for zi in zile:
#     url = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-" + str(zi) + "-ianuarie-ora-13-00/"

# url = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/'


driver.get(
     f'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{ziua}-ianuarie-ora-13-00/')

lista1 = []

lista2 = []

for i in range (1,44): # rows
    for j in range (1,5): # columns
        data = lista1.append(driver.find_element_by_xpath(
            f"//table/tbody/tr[{i}]/td[{j}]").text)

# print(lista1)

lista2 = [lista1[i:i+5] for i in range(0, len(lista1), 5)]

print(lista2)

# de studiat export to xls folosind pandas?
# df = pd.DataFrame()


driver.close()












