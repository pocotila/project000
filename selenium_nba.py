from selenium import webdriver

import pandas as pd

import xlsxwriter

driver = webdriver.Chrome(executable_path='C:\Chrome\chromedriver.exe')

df = pd.DataFrame(columns=['Player', 'Salary', 'Year'])  # creates master dataframe

for yr in range(1990, 1991):
    page_num = str(yr) + '-' + str(yr + 1) + '/'
    url = 'https://hoopshype.com/salaries/players/' + page_num
    driver.get(url)

    players = driver.find_elements_by_xpath('//td[@class="name"]')
    salaries = driver.find_elements_by_xpath('//td[@class="hh-salaries-sorted"]')

    players_list = []
    for p in range(len(players)):
        players_list.append(players[p].text)

    salaries_list = []
    for s in range(len(salaries)):
        salaries_list.append(salaries[s].text)

    data_tuples = list(zip(players_list[1:], salaries_list[1:]))  # list of each players name and salary paired together
    temp_df = pd.DataFrame(data_tuples, columns=['Player', 'Salary'])  # creates dataframe of each tuple in list
    temp_df['Year'] = yr  # adds season beginning year to each dataframe
    df = df.append(temp_df)  # appends to master dataframe

driver.close()