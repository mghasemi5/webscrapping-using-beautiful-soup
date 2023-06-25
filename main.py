import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://finance.yahoo.com'
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')

#scrap the S&P 500 price
sp_price_element = soup.find('fin-streamer', {'data-symbol': '^GSPC', 'data-field': 'regularMarketPrice'})
sp_price = sp_price_element['value']
#scrap the DOW30 price
dow30_price_element = soup.find('fin-streamer', {'data-symbol': '^DJI', 'data-field': 'regularMarketPrice'})
dow30_price = dow30_price_element['value']
#scrap the nasdaq price
nasdaq_price_element = soup.find('fin-streamer', {'data-symbol': '^IXIC', 'data-field': 'regularMarketPrice'})
nasdaq_price = nasdaq_price_element['value']
#scrap the RUSSEL price
russel_price_element = soup.find('fin-streamer', {'data-symbol': '^RUT', 'data-field': 'regularMarketPrice'})
russel_price = russel_price_element['value']

#printing the data
print('The current S&P 500 price is:', sp_price)
print('The current DOW30 price is:', dow30_price)
print('The current nasdaq price is:', nasdaq_price)
print('The current RUSSEL2000 price is:', russel_price)


# Creating a DataFrame
data = {
    'Symbol': ['S&P 500', 'Dow Jones', 'Nasdaq Composite','RUSSEL 2000'],
    'Price': [sp_price, dow30_price, nasdaq_price,russel_price]
}
df = pd.DataFrame(data)
# Saving data to Excel
file_name = 'stock_prices.xlsx'
df.to_excel(file_name, index=False)
print('Data saved to', file_name)