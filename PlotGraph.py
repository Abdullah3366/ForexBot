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

def plot(df, SMA_list, EMA_list):
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
    x=df.index, open = df["Open"], high = df["High"], low = df["Low"], close=df["Close"],
    line=dict(width=1), opacity=1,
    increasing_fillcolor='#24A06B',
    decreasing_fillcolor="#CC2E3C",
    increasing_line_color='#2EC886',  
    decreasing_line_color='#FF3A4C')
    )

    for sma in SMA_list:
        fig.add_trace(go.Scatter(x=df.index, y=df[f"SMA_{sma}"], name=f"SMA_{sma}", line=dict(width=2)))

    for ema in EMA_list:
        fig.add_trace(go.Scatter(x=df.index, y=df[f"EMA_{ema}"], name=f"EMA_{ema}", line=dict(width=2)))

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

    fig.show()

df_plot = df.iloc[-500:].copy()
df_plot_bid = df_plot['bid'].copy()
#df_plot_bid['MA5'] = df_plot_bid["Close"].rolling(5).mean()
df_plot_bid['MA16'] = TA.SMA(df_plot_bid, 16)
df_plot_bid['MA64'] = TA.SMA(df_plot_bid, 64)
df_plot_bid['EMA5'] = TA.EMA(df_plot_bid, 5)
#MACD = TA.MACD(df_plot_bid)
#print(MACD)

#print(df_plot_bid)

#if __name__ == "__main__":

    