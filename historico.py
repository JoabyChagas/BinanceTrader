import binance
import pandas
import matplotlib.pyplot as plt
from setup import API_Key, Secret_Key

client = binance.Client(API_Key, Secret_Key)

# pegando os dados
df = pandas.DataFrame(client.get_historical_klines('BTCBRL', "1d", "1 Jan, 2024", "1 Fev, 2024"))
df = df.iloc[:, :6]
df.columns = ['date_open', 'Open', 'High', 'Low', 'Close', 'Volume']
df = df.set_index('date_open')
df.index = pandas.to_datetime(df.index, unit='ms')
df = df.astype(float)

print(df)
