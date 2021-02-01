from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import xlsxwriter

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get('https://www.bnr.ro/files/xml/nbrfxrates2019.htm')

# drivers = driver.find_element_by_xpath('//table')

# drivers = driver.find_element_by_xpath('//table/tbody//tr['+str(i)+']/td['str(j)+']/div'))

lista = []
dfs = []
dictionar ={}
data = driver.find_element_by_xpath('//table').text.split('\n')

for i in range(0,len(data),33):
    dictionar[data[i]]=data[i]
    lista.append(dictionar)

for value in lista:
    df = pd.DataFrame(data=value)
    dfs.append(df)

writer = pd.ExcelWriter("C:/Users/george.cergau/PycharmProjects/quizz/xl_sheet_bnr.xls", engine='xlsxwriter')

for i, value in enumerate(dfs):
    dfs.to_excel(writer,sheet_name=str(i))

writer.save()


# lista.append(driver.find_element_by_xpath('//table/tbody//tr['+str(i)+']/td['+str(j)+']/div'))

#for text in lista:
 #   element = text.text
  #  lista2.append(element)


#print(lista2)



# /html/body/div[4]/table/thead/tr/th/div
# //*[@id="Data_table"]/table/thead/tr/th[33]/div

