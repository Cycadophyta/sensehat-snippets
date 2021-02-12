import plotly.express as px
import pandas as pd

data = pd.read_csv('senselog_2020-08-09.csv')

pd.to_datetime(data.datetime)

print(data.head())

temp = px.bar(data, x='datetime', y='temp')
temp.show()