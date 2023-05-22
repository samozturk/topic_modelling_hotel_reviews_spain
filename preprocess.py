    '''Script to fix incorrect date values in `date` column.
    '''
import re

import numpy as np
import pandas as pd

# Read the data and get necessary fields
df = pd.read_csv('merged_reviews.csv')
df = df[['date', 'review_text', 'rating']]

df = df.dropna()

# Fix the faulty dates of the last month(May)
proper_dates = []
pattern = r'\d{4}$'
# Iterate through date column
for date in df['date'].values:
    # Search for values that ends with 4 numbers which is a year
    if re.search(pattern, date):
        proper_dates.append(date)
    # 
    else:
        proper_dates.append(f'{date[:3]} 2023')

df['date'] = np.array(proper_dates)

df.to_csv('final.csv', index=False)