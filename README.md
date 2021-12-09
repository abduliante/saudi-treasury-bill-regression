# Saudi Central Bank Treasury Bill Prediction

## Abstract:
Saudi Central Bank (SAMA) offers short-term securities that mature in one year or less called **Treasury Bill** (T-Bills).
Unlike Treasury bonds which has long-term maturity, T-Bills are purchased for a price less than their face value (called discount rate) and then when they mature, the treasury (SAMA) pays the investor the full face value.

This project aims to predict treasury bill yields. The data has been obtained from SAMA official website which we had to scrape to perform our modeling.

## Research Hypothesis:
In our project, we try to hypothesize if inflation and money supply rates influence treasury bill returns. Verifying the hypothesis would help us create a model that predict treasury yields.
Since T-Bills are considered safe securities, our model; as a result, would help future investors to confidently choose the right time to invest in these short-term securities.

## Data Description
Our data will be scraped from [Saudi Central Bank](https://www.sama.gov.sa/en-US/FinExc/Pages/default.aspx) website using BeautifulSoup4 tool. The data spans from 2010 to 2021. There are approximately 4000+ rows and 7 columns.


| Feature | Description |
| -   | - |
| date | identifies the date of each row |
| repo_rate | repersent the repurchase agreement rate for a specific period |
| money_supply_rate | money supply growth rate (of total volume of money held by the public) for specific period |
| inflation_rate | indicates the inflation rate for a specific period |
| maturity_term | maturity term for a T-bill (5 columns) |


## Tools:
The prediction is going to be delivered on an IPython Notebook. Tools to be used are:
* Python 3.7
* BeautifulSoup4 -- Data scraping
* Selenium
* Pandas
* Numpy
* Scikit-learn
* Matplotlib
* Seaborn
