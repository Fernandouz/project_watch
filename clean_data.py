import pandas as pd
from datetime import datetime

date = datetime.now().strftime('%d_%m')

csv = f"watches_prices_{date}.csv"

df = pd.read_csv(csv)

price = df['Price']

price = price.replace('COTE',"", inplace=False,regex=True).replace("€","", inplace=False,regex=True)

price = price.replace('\u202F',"", inplace=False,regex=True)

price = pd.to_numeric(price)

df['Price'] = price

df.to_csv(csv, index=False)

# print(df)

mean_brand = df.groupby(['Brand']).mean(['Price'])

# print(mean_brand.min(), mean_brand.max())
min_price_rows = mean_brand[mean_brand['Price'] == mean_brand['Price'].min()]
max_price_rows = mean_brand[mean_brand['Price'] == mean_brand['Price'].max()]

print(min_price_rows, max_price_rows)

