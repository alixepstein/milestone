import streamlit as st

import pandas as pd

import requests

import json

import plotly
import plotly.express as px
import numpy as np



st.title('Stock prices')
symbol_input = st.text_input(label="Ticker", help="Enter the stock ticker symbol")
	
def display_data (symbol_input):
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
    fig = px.line(x=x, y=y, labels={'x':'Date', 'y':'Closing Price'})
    st.plotly_chart(fig, use_container_width=True)

if st.button('Get info'):
    display_data(symbol_input)
