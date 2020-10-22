import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot

init_notebook_mode(connected=True)
import plotly.plotly as py
import plotly
import pandas as pd
import datetime


df = pd.read_csv("TSLA.csv")

df['date'] = df['date'].astype('str')
df['high'] = df['high'].astype('double')
df['low'] = df['low'].astype('double')

date2 = []
for i in df['date']:
    new_date = datetime.datetime.strptime(i, "%d/%m/%Y").strftime("%Y-%m-%d")
    date2.append(new_date)

df['date'] = df['date'].str.replace('/', '-')
df['date'] = date2
df.fillna(0)
df.head()