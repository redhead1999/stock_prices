import streamlit as st
from datetime import date

import yfinance as yf
from plotly import graph_objs as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Котировки Акций')

stocks = ('AAPL', 'AMD', 'AMZN', 'BABA', 'FB', 'GOOG', 'KO', 'MSFT', 'PINS', 'TSLA', 'YNDX')
selected_stock = st.selectbox('Выберите акцию', stocks)

@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

	
data_load_state = st.text('Загрузка...')
data = load_data(selected_stock)
data_load_state.text('Загрузка... Готово!')

st.subheader('Данные акции')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text='Данные временных рядов с выбором диапазона', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
	
plot_raw_data()