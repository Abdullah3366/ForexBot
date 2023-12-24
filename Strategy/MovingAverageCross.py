import plotly.graph_objects as go
from finta import TA
import pandas as pd 

df = pd.read_pickle('./His_USDJPY_4H_2023.pkl')

def is_trade(row):
    if row.DIFF >= 0 and row.DIFF_Prev < 0:
        return True
    if row.DIFF <= 0 and row.DIFF_Prev > 0:
        return True
    return False


#df_500 = df.iloc[-500:].copy()
df_bid = df['bid'].copy()

df_bid['MA16'] = TA.SMA(df_bid, 16)
df_bid['MA64'] = TA.SMA(df_bid, 64)
df_bid['EMA5'] = TA.EMA(df_bid, 5)


df_bid['DIFF'] = df_bid.MA16 - df_bid.MA64
df_bid['DIFF_Prev'] = df_bid.DIFF.shift(1)

df_bid['IS_TRADE'] = df_bid.apply(is_trade, axis=1)

df_trades = df_bid[df_bid.IS_TRADE==True].copy()

print(df_trades)
