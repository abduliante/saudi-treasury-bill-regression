import pandas as pd
import numpy as np

# read csv
df_inflation = pd.read_csv("../data/raw/inflation_rate_2009_2021.csv")
df_money_supply = pd.read_csv("../data/raw/money_supply.csv")
df_repo = pd.read_csv("../data/processed/repo_dates_all.csv")
df_bills = pd.read_csv("../data/raw/t_bills.csv")

# convert date
df_inflation['inflation_date'] = pd.to_datetime(df_inflation['inflation_date'])
df_money_supply['money_date'] = pd.to_datetime(df_money_supply['money_date'])
df_repo['repo_date'] = pd.to_datetime(df_repo['repo_date'])
df_bills['Period'] = pd.to_datetime(df_bills['Period'])

# date consistancy
df_b = df_bills[df_bills['Period'].isin(pd.date_range('2010-01-01','2021-10-01'))]
df_m = df_money_supply[df_money_supply['money_date'].isin(pd.date_range('2010-01-01','2021-12-01'))]
df_r = df_repo[df_repo['repo_date'].isin(pd.date_range('2010-01-01','2021-12-01'))]
df_i = df_inflation[df_inflation['inflation_date'].isin(pd.date_range('2010-01-01','2021-12-01'))]

# join and merge
df = df_i.join(df_m).join(df_r).merge(df_b, right_on='inflation_date', left_on='Period')

# drop money_date, repo_date
df.drop(['money_date', 'repo_date',], axis=1, inplace=True)

# export csv
df.to_csv('../data/processed/processed_final.csv', index=False)