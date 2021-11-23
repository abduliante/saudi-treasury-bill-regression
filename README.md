# Saudi Central Bank Treasury Bill Prediction

## Abstract:
Saudi Centeral Bank (SAMA) offers short-term securities that mature in one year or less called *Treasury Bill*(T-Bills).
Unlike Treasury bonds which has long-term maturity, T-Bills are purchased for a price less than their face value (called discount rate) and then when they mature, the treasury (SAMA) pays the investor the full face value.

This project aims to predict treasury bill yields. The data has been obtained from SAMA official website which we had to scrape to perform our modeling.

## Research Hypothesis:
In our project, we try to hypothesize if inflation and money supply rates influence treasury bill returns. Verifying the hypothesis would help us create a model that predict treasury yields.
Since T-Bills are considered safe securities, our model; as a result, would help future investors to confidently choose the right time to invest in these securities.

## Data Description
Our data will be scraped from [Saudi Central Bank](https://www.sama.gov.sa/en-US/FinExc/Pages/default.aspx) website using BeautifulSoup4 tool. The data spans from 2009 to 2021. There are approximately 144 rows and 6 columns.

< ADD DATA TABLE >

## Tools:
The prediction is going to be delivered on an IPython Notebook. Tools to be used are:
* Python 3.7
* BeautifulSoup4 -- Data scraping
* Pandas
* Numpy
* Scikit-learn
* Matplotlib
* Seaborn
