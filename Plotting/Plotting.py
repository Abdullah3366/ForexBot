import plotly.graph_objects as go
from finta import TA
import pandas as pd 

df = pd.read_pickle('./His_USDJPY_4H_2023.pkl')
#print(df.describe())

def is_trade(row):
    if row.DIFF >= 0 and row.DIFF_Prev < 0:
        return True
    if row.DIFF <= 0 and row.DIFF_Prev > 0:
        return True
    return False


df_plot = df.iloc[-500:].copy()
df_plot_bid = df_plot['bid'].copy()
#df_plot_bid['MA5'] = df_plot_bid["Close"].rolling(5).mean()
df_plot_bid['MA16'] = TA.SMA(df_plot_bid, 16)
df_plot_bid['MA64'] = TA.SMA(df_plot_bid, 64)
df_plot_bid['EMA5'] = TA.EMA(df_plot_bid, 5)
#MACD = TA.MACD(df_plot_bid)
#print(MACD)

#print(df_plot_bid)

df_plot_bid['DIFF'] = df_plot_bid.MA16 - df_plot_bid.MA64
df_plot_bid['DIFF_Prev'] = df_plot_bid.DIFF.shift(1)

df_plot_bid['IS_TRADE'] = df_plot_bid.apply(is_trade, axis=1)

df_trades = df_plot_bid[df_plot_bid.IS_TRADE==True].copy()

print(df_trades)

fig = go.Figure()
fig.add_trace(go.Candlestick(
    x=df_plot_bid.index, open = df_plot_bid["Open"], high = df_plot_bid["High"], low = df_plot_bid["Low"], close=df_plot_bid["Close"],
    line=dict(width=1), opacity=1,
    increasing_fillcolor='#24A06B',
    decreasing_fillcolor="#CC2E3C",
    increasing_line_color='#2EC886',  
    decreasing_line_color='#FF3A4C')
    )

fig.add_trace(go.Scatter(x=df_plot_bid.index, y=df_plot_bid["MA16"], line=dict(color='orange', width=1)))
fig.add_trace(go.Scatter(x=df_plot_bid.index, y=df_plot_bid["MA64"], line=dict(color='blue', width=1)))
#fig.add_trace(go.Scatter(x=df_plot_bid.index, y=df_plot_bid["EMA5"], line=dict(color='blue', width=1)))

fig.update_xaxes(
        showgrid=False,
        rangeslider_visible=True,
        rangebreaks=[
            # NOTE: Below values are bound (not single values), ie. hide x to y
            dict(bounds=["sat", "mon"]),  # hide weekends, eg. hide sat to before mon
            #dict(bounds=[16, 9.5], pattern="hour"),  # hide hours outside of 9.30am-4pm
            # dict(values=["2019-12-25", "2020-12-24"])  # hide holidays (Christmas and New Year's, etc)
        ]
    )

fig.update_layout(
    font=dict(size=10, color="#e1e1e1"),
    title='USDJPY',
    yaxis_title=f'Price',
    plot_bgcolor="#1e1e1e",
    paper_bgcolor="#1e1e1e"
    )

#fig.show()
