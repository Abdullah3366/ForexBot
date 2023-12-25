import plotly.graph_objects as go
from finta import TA
import pandas as pd 
import PlotGraph


df = pd.read_pickle('./His_USDJPY_4H_2023.pkl')

def is_trade(row):
    if row.DIFF >= 0 and row.DIFF_Prev < 0:
        return True
    if row.DIFF <= 0 and row.DIFF_Prev > 0:
        return True
    return False

def add_SMA(df, period):
    for pr in period:
        df[f"SMA_{pr}"] = TA.SMA(df, int(pr))

def add_EMA(df, period):
    for pr in period:
        df[f"EMA_{pr}"] = TA.EMA(df, int(pr))


df_bid = df['bid'].copy()

SMA_list = ["16", "32"]
EMA_list = ["16", "32"]

add_SMA(df_bid, SMA_list)
add_EMA(df_bid, EMA_list)

PlotGraph.plot(df_bid, SMA_list, EMA_list)


df_bid['DIFF'] = df_bid.SMA_16 - df_bid.SMA_32
df_bid['DIFF_Prev'] = df_bid.DIFF.shift(1)

df_bid['IS_TRADE'] = df_bid.apply(is_trade, axis=1)

df_trades = df_bid[df_bid.IS_TRADE==True].copy()

print(df_trades)
