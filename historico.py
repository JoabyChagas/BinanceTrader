import pandas
import binance
from setup import API_Key, Secret_Key
import plotly.graph_objects as go
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import warnings
warnings.filterwarnings('ignore')
pandas.options.display.float_format = '${:,.2f}'.format

# Conecta a API da Binance
client = binance.Client(API_Key, Secret_Key)

# pegando os dados
df = pandas.DataFrame(client.get_historical_klines('BTCUSDT', "1d", "1 Jan, 2018", "1 Jan, 2024"))
df = df.iloc[:, :6]
df.columns = ['date_open', 'Open', 'High', 'Low', 'Close', 'Volume']
df = df.set_index('date_open')
df.index = pandas.to_datetime(df.index, unit='ms')
df = df.astype(float)
df.reset_index(inplace=True)
ndf = df[['date_open', 'Close']]
ndf.rename(columns={'date_open': 'ds', 'Close': 'y'}, inplace=True)

# Criando Gráfico de preço de fechamento
fig = go.Figure()
fig.add_trace(go.Scatter(x=ndf['ds'], y=ndf['y']))
#fig.show()

# Modelo de trinamento
model = Prophet( seasonality_mode='multiplicative')
model.fit(ndf)

df_futuro = model.make_future_dataframe(periods=30)
previsao = model.predict(df_futuro)

print(previsao[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
#plot_plotly(model, previsao).show()
#plot_components_plotly(model, previsao).show()