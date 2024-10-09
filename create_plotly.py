import plotly.graph_objects as go
import yfinance as yf
from plotly.subplots import make_subplots

# トップ6社のティッカーシンボル
stocks = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'NVIDIA': 'NVDA',
    'Amazon': 'AMZN',
    'Meta': 'META',
    'Alphabet': 'GOOGL'
}

# 株価データを取得
stock_data = {}
for name, ticker in stocks.items():
    stock_data[name] = yf.download(ticker, start='2020-01-01', end='2024-10-09')

# インタラクティブなグラフの作成
fig = make_subplots(rows=1, cols=1)

# Appleのローソク足データをデフォルトで追加
fig.add_trace(go.Candlestick(x=stock_data['Apple'].index,
                             open=stock_data['Apple']['Open'],
                             high=stock_data['Apple']['High'],
                             low=stock_data['Apple']['Low'],
                             close=stock_data['Apple']['Close'],
                             name='Apple'))

# レイアウトの設定
fig.update_layout(
    title="Top 6 Companies Stock Prices (Candlestick)",
    xaxis_title="Date",
    yaxis_title="Stock Price (USD)",
    updatemenus=[
        {
            "buttons": [
                {
                    "args": [{"x": [stock_data['Apple'].index],
                              "open": [stock_data['Apple']['Open']],
                              "high": [stock_data['Apple']['High']],
                              "low": [stock_data['Apple']['Low']],
                              "close": [stock_data['Apple']['Close']],
                              "name": "Apple"}],
                    "label": "Apple",
                    "method": "restyle"
                },
                {
                    "args": [{"x": [stock_data['Microsoft'].index],
                              "open": [stock_data['Microsoft']['Open']],
                              "high": [stock_data['Microsoft']['High']],
                              "low": [stock_data['Microsoft']['Low']],
                              "close": [stock_data['Microsoft']['Close']],
                              "name": "Microsoft"}],
                    "label": "Microsoft",
                    "method": "restyle"
                },
                {
                    "args": [{"x": [stock_data['NVIDIA'].index],
                              "open": [stock_data['NVIDIA']['Open']],
                              "high": [stock_data['NVIDIA']['High']],
                              "low": [stock_data['NVIDIA']['Low']],
                              "close": [stock_data['NVIDIA']['Close']],
                              "name": "NVIDIA"}],
                    "label": "NVIDIA",
                    "method": "restyle"
                },
                {
                    "args": [{"x": [stock_data['Amazon'].index],
                              "open": [stock_data['Amazon']['Open']],
                              "high": [stock_data['Amazon']['High']],
                              "low": [stock_data['Amazon']['Low']],
                              "close": [stock_data['Amazon']['Close']],
                              "name": "Amazon"}],
                    "label": "Amazon",
                    "method": "restyle"
                },
                {
                    "args": [{"x": [stock_data['Meta'].index],
                              "open": [stock_data['Meta']['Open']],
                              "high": [stock_data['Meta']['High']],
                              "low": [stock_data['Meta']['Low']],
                              "close": [stock_data['Meta']['Close']],
                              "name": "Meta"}],
                    "label": "Meta",
                    "method": "restyle"
                },
                {
                    "args": [{"x": [stock_data['Alphabet'].index],
                              "open": [stock_data['Alphabet']['Open']],
                              "high": [stock_data['Alphabet']['High']],
                              "low": [stock_data['Alphabet']['Low']],
                              "close": [stock_data['Alphabet']['Close']],
                              "name": "Alphabet"}],
                    "label": "Alphabet",
                    "method": "restyle"
                }
            ],
            "direction": "down",
            "showactive": True
        }
    ],
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(visible=True),
        type="date"
    )
)

# グラフをHTMLファイルとして保存
fig.write_html("top6_stock_prices.html")
