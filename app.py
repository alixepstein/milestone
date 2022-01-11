import streamlit as stimport pandas as pdimport requestsimport json
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
st.title('Stock prices')symbol_input = st.text_input(label="Ticker", help="Enter the stock ticker symbol")


payload = {'function': 'TIME_SERIES_DAILY', 'symbol': symbol_input, 'datatype': 'csv', 'apikey': 'GNN6K0ZEGN5RICF1'}
url = 'https://www.alphavantage.co/query?'
r = requests.get(url, params = payload)
rurl = r.url
df = pd.read_csv(rurl)

df = pd.read_csv(rurl, usecols = ['timestamp', 'close'])
df['timestamp'] = pd.to_datetime(df['timestamp'])

x = df['timestamp']
y = df['close']
p = figure(title="Daily Closing Prices", x_axis_label='Date', y_axis_label='Closing Price')
p.line(x, y, line_width=2)
st.bokeh_chart(p, use_container_width=True)