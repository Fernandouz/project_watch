import pandas

data = pandas.read_csv('watches_prices_15_04.csv')

prices = data['Price']

prices = prices.str.replace('COTE', '').str.strip().str.replace('\u202F', '')

print(prices)

data['Price'] = prices

print(data)

data.to_csv(f"/Users/hugo/PycharmProjects/project_watches/watches_prices_15_04_2.csv", index=False)