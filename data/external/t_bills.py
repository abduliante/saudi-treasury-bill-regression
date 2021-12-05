from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv


# initalize driver
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://www.sama.gov.sa/en-US/GovtSecurity/pages/SAMABills.aspx?&&p_SAMABillYear=8_2020&p_SAMABillPeriod=20200901%2021%3a00%3a00&&PageFirstRow=1&View=4ee023c6-55dc-4522-bbc9-07e0458448c5')


# container
bills = []

# handle page navigation, append items
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

# close driver
driver.close()


# get column names
colnames = []
for i in sama_bill_table.find_all('tr')[0]:
    colnames.append(i.text)

# for i in sama_bill_table.find_all('tr')[1:]:
#     for j in i.find_all('td'):
#         for link_text in j.find_all('a'):
#             print(link_text.text)


# split bill list into dates and yields
def date_yields_chop(l):
    date = []
    t_yields = []
    
    # convert yields from string to float
    for i in l:
        try:
            float(i)
            t_yields.append(i)
        except ValueError: #if exception arise, means that it's a string
            date.append(i)
    # remove "Year" string, not needed
    for dates in date:
        if dates.startswith('Year'): 
            date.remove(dates)
    return date, t_yields

# dates
date_yields_chop(bills)[0]

# yields
date_yields_chop(bills)[1]

len(date_yields_chop(bills)[1])

# split list into 5 chunks for 1st, 4th, 13th, 26th and 52nd weeks respectively
def split_yields(l):
    res = [l[i:i+5] for i in range(0, len(l), 5)]
    return res

# export csv
with open('t_bills.csv', 'a') as f:
    writer = csv.writer(f)
    header = colnames
    writer.writerow(header)
    for i in range(len(date_yields_chop(bills)[0])):
        week1, week4, week13, week26, week52 = split_yields(date_yields_chop(bills)[1])[i]
        row = [date_yields_chop(bills)[0][i], week1, week4, week13, week26, week52]
        writer.writerow(row)