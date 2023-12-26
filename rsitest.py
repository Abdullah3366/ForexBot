import plotly.graph_objects as go
from finta import TA
import pandas as pd 
import PlotGraph


df = pd.read_pickle('./His_USDJPY_1H_2023.pkl')
df_bid = df['bid'].copy()

RSI = TA.RSI(df_bid, 34)

print(RSI)