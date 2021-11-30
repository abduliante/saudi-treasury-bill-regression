from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://www.sama.gov.sa/en-US/GovtSecurity/pages/SAMABills.aspx?&&p_SAMABillYear=8_2020&p_SAMABillPeriod=20200901%2021%3a00%3a00&&PageFirstRow=1&View=4ee023c6-55dc-4522-bbc9-07e0458448c5')


soup = BeautifulSoup(driver.page_source, 'html.parser')
sama_bill_table = soup.find('table', class_='grid')

bills = []


for i in range(1,100):

    j = 0
    driver.get(driver.current_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    sama_bill_table = soup.find('table', class_='grid')
    
    # time.sleep(2)

    for tr in sama_bill_table.find_all('tr')[1:]:
        for row in tr.find_all('td'):
            bills.append(row.text)

    try:
        next_page = driver.find_elements_by_xpath(f"//div[@class='Paging']/a[{i+j}]")
        j+=1
        next_page[0].click()
    except IndexError:
        next_page = driver.find_elements_by_xpath("//div[@class='Paging']/a[2]")
        next_page[0].click()

    time.sleep(2)



# colnames
for i in sama_bill_table.find_all('tr')[0]:
    print(i.text)


# for i in sama_bill_table.find_all('tr')[1:]:
#     for j in i.find_all('td'):
#         for link_text in j.find_all('a'):
#             print(link_text.text)


def date_yields_chop(l):
    date = []
    t_yields = []
    for i in l:
        try:
            float(i)
            t_yields.append(i)
        except ValueError:
            date.append(i)
    for dates in date:
        if dates.startswith('Year'):
            date.remove(dates)
    return date, t_yields

# dates
date_yields_chop(bills)[0]

# yields
date_yields_chop(bills)[1]

driver.close()