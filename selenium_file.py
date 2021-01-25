from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.cel.ro/index.php?main_page=login')

get_element1 = driver.find_element_by_id('firstname')
get_element1.send_keys('Ana')

get_element2 = driver.find_element_by_id('lastname')
get_element2.send_keys('Maria')

get_element3 = driver.find_element_by_id('email_address')
get_element3.send_keys('alfabet@tester.ro')

get_element4 = driver.find_element_by_id('customers_gender')
get_element4.send_keys('Doamna')

get_element5 = driver.find_element_by_id('telephone')
get_element5.send_keys('0721330799')

get_element6 = driver.find_element_by_id('street_address')
get_element6.send_keys('Iasi1')

get_element7 = driver.find_element_by_id('entry_suburb')
get_element7.send_keys('Ploiesti')

from selenium.webdriver.common.keys import Keys
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)

get_element8 = driver.find_element_by_xpath('//*[@id="cont_nou"]/tbody[2]/tr[1]/td/div[2]/label/input')
get_element8.click()

get_element1.submit()