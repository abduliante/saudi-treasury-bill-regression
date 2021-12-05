from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv 


driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get("https://www.sama.gov.sa/en-US/Indices/Pages/InflationRate.aspx?&&p_SAMALastUpdatedDate=20200715%2021%3a00%3a00&&PageFirstRow=1&View=c1ab60f3-6a13-4471-b117-a8483cfaca65")

# driver.get(driver.current_url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

inflation_rate_table = soup.find('table', class_='grid')
inflation_rate_table
inflation_rate_table.find_all('td')[::2]
inflation_rate_table.find_all('td')[1:][::2]


infdate = []
infrate = []

for i in range(1,100):
    j = 0
    
    driver.get(driver.current_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    inflation_rate_table = soup.find('table', class_='grid')

    for infd in inflation_rate_table.find_all('td')[::2]:
        infdate.append(infd.text)
    for infr in inflation_rate_table.find_all('td')[1:][::2]:
        infrate.append(infr.text)

    try:
        next_page = driver.find_elements_by_xpath(f"//div[@class='Paging']/a[{i+j}]")
        j+=1
        next_page[0].click()
    except IndexError:
        next_page = driver.find_elements_by_xpath(f"//div[@class='Paging']/a[2]")
        next_page[0].click()

    time.sleep(2)
driver.close() 



with open('inflation_rate.csv', 'a') as f:
    writer = csv.writer(f)
    header = ['inflation_date', 'inflation_rate']
    writer.writerow(header)

    for i in range(len(infdate)):
        row = [infdate[i], infrate[i]]
        writer.writerow(row)