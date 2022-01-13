import streamlit as st
import pandas as pdimport requestsimport json

from bokeh.plotting import figure, show

from bokeh.io import output_notebook
st.title('Stock prices')symbol_input = st.text_input(label="Ticker", help="Enter the stock ticker symbol")


payload = {'function': 'TIME_SERIES_DAILY', 'symbol': symbol_input, 'apikey': 'GNN6K0ZEGN5RICF1'}
url = 'https://www.alphavantage.co/query?'
r = requests.get(url, params = payload)

data = r.json()
#tsd = data.get('Time Series (Daily)')
tsd = data['Time Series (Daily)']

df = pd.DataFrame.from_dict(tsd, orient = 'index')


df.index = pd.to_datetime(df.index)

x = df.index
y = df['4. close']


p = figure(title="Daily Closing Prices", x_axis_label='Date', y_axis_label='Closing Price')
p.line(x, y, line_width=2)
st.bokeh_chart(p, use_container_width=True)