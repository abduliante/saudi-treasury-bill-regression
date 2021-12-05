from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv 


# initalize driver
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get("https://www.sama.gov.sa/en-US/Indices/Pages/MoneySupply.aspx")


# containers
mdates = []
mrates = []

# handle page navigation append items
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

# close driver
driver.close() 

# verify integrity
print(len(mdates) == len(mrates))

# export csv
with open('money_supply.csv', 'a') as f:
    writer = csv.writer(f)
    header = ['money_date', 'money_rate']
    writer.writerow(header)
    for i in range(len(mdates)):
        row = [mdates[i], mrates[i]]
        writer.writerow(row)