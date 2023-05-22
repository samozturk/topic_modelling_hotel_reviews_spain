    '''Script to split `final.csv` to different periods and save them as csv files.
    '''
import pandas as pd

df = pd.read_csv('final.csv')
df['date'] = pd.to_datetime(df['date'])

precovid = df[(df['date'] < '2020-03-01') & ((df['date'] > '2014-01-01'))]
print(f"{len(precovid)} rows of pre-covid reviews")
precovid.to_csv('precovid.csv')

covid = df[(df['date'] > '2020-03-01') & ((df['date'] < '2022-01-01'))]
print(f"{len(covid)} rows of covid reviews")
covid.to_csv('covid.csv')

post_covid = df[((df['date'] > '2022-01-01'))]
print(f"{len(post_covid)} rows of post-covid reviews")
post_covid.to_csv('postcovid.csv')
