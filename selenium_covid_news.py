import xlsxwriter
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.minimize_window()

for data in range(13, 20):
    try:
        driver.get(f'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{str(data)}-ianuarie-ora-13-00/')

        with xlsxwriter.Workbook('covid.xlsx') as workbook:
            worksheet = workbook.add_worksheet()

        for iterator in range(1, 45):
            table = driver.find_element_by_xpath(f"/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[{iterator}]").text
            print(table)
            worksheet.write_row(iterator, 0, table)
    except:
        print(f"Eroare citire la data {data} Ianuarie")

driver.quit()
