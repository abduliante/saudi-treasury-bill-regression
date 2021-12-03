from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

# initialize driver
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://www.sama.gov.sa/en-US/Repo/pages/OfficialRepoRate.aspx?&&p_SAMAPublishDate=20060131%2021%3a00%3a00&&PageFirstRow=1&View=7aa67fe6-8409-4caa-b769-4094aae0daa5')

# empty lists for repo date, rate, and change
rdate = []
rrate = []
rchange = []


# handle page navigation and append items
for i in range(1,100):
    
    j = 0
    driver.get(driver.current_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    repo_rate_table = soup.find('table', class_='grid')
    
    # time.sleep(2)
    for items in repo_rate_table.find_all('tr')[1:]:
        for date in items.find_all('td')[0]:
            # print(f'DATE: {date.text}')
            rdate.append(date.text)
        for rate in items.find_all('td')[1]:
            # print(f'RATE: {rate.text}')
            rrate.append(rate.text)
        for change in items.find_all('td')[2]:
            # print(f'CHANGE: {change.text}')
            rchange.append(change.text)

    try:
        next_page = driver.find_elements_by_xpath(f"//div[@class='Paging']/a[{i+j}]")
        j+=1
        next_page[0].click()
    except IndexError:
        next_page = driver.find_elements_by_xpath("//div[@class='Paging']/a[2]")
        next_page[0].click()

    time.sleep(2)

# check integrity:
print(len(rchange) == len(rrate) == len(rdate))

# close driver
driver.close()

# export csv
with open('repo_rate.csv', 'a') as f:
    writer = csv.writer(f)
    header = ['repo_date', 'repo_rate', 'repo_change']
    writer.writerow(header)
    for i in range(len(rdate)):
        row = [rdate[i], rrate[i], rchange[i]]
        writer.writerow(row)
