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
    stock_data[name] = yf.download(ticker, start='2020-01-01', end='2023-01-01')

# インタラクティブなグラフの作成
fig = make_subplots(rows=1, cols=1)

# Appleのデータをデフォルトで追加
fig.add_trace(go.Scatter(x=stock_data['Apple'].index, y=stock_data['Apple']['Close'], name='Apple'))

# レイアウトの設定
fig.update_layout(
    title="Top 6 Companies Stock Price Over Time",
    xaxis_title="Date",
    yaxis_title="Stock Price (USD)",
    updatemenus=[
        {
            "buttons": [
                {
                    "args": [{"y": [stock_data['Apple']['Close']], "name": "Apple"}],
                    "label": "Apple",
                    "method": "update"
                },
                {
                    "args": [{"y": [stock_data['Microsoft']['Close']], "name": "Microsoft"}],
                    "label": "Microsoft",
                    "method": "update"
                },
                {
                    "args": [{"y": [stock_data['NVIDIA']['Close']], "name": "NVIDIA"}],
                    "label": "NVIDIA",
                    "method": "update"
                },
                {
                    "args": [{"y": [stock_data['Amazon']['Close']], "name": "Amazon"}],
                    "label": "Amazon",
                    "method": "update"
                },
                {
                    "args": [{"y": [stock_data['Meta']['Close']], "name": "Meta"}],
                    "label": "Meta",
                    "method": "update"
                },
                {
                    "args": [{"y": [stock_data['Alphabet']['Close']], "name": "Alphabet"}],
                    "label": "Alphabet",
                    "method": "update"
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
