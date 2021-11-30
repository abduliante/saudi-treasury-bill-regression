from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get("https://www.sama.gov.sa/en-US/Indices/Pages/MoneySupply.aspx")


# handle page navigation
mdates = []
mrates = []

for i in range(1,100):
    j = 0
    
    driver.get(driver.current_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    money_supply_table = soup.find('table')

    for rd in money_supply_table.find_all('td')[1:][::2]:
        mdates.append(rd.text)
    for rr in money_supply_table.find_all('td')[1:][::-2][::-1]:
        mrates.append(rr.text)

    try:
        next_page = driver.find_elements_by_xpath(f"//div[@class='Paging']/a[{i+j}]")
        j+=1
        next_page[0].click()
    except IndexError:
        next_page = driver.find_elements_by_xpath(f"//div[@class='Paging']/a[2]")
        next_page[0].click()

    time.sleep(2)
driver.close() 

print(len(mdates) == len(mrates))