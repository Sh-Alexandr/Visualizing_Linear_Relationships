# pip install pandas
# pip install numpy
# pip install dash
# pip install matplotlib
# pip install seaborn
# pip install plotly
# pip install statsmodels

import pandas as pd
# import numpy as np
from plotly import express as px
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Instagram.csv", encoding = 'latin1')
data = data.dropna()
print(data.head())

figure = px.scatter(data_frame = data,
                    x="Impressions",
                    y="Likes",
                    size="Likes",
                    trendline="ols",
                    title = "Relationship Between Likes and Impressions")
figure.show()
figure.write_html('first_figure.html', auto_open=False)

plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Relationship Bewtween Likes & Impressions")
sns.regplot(x="Impressions", y="Likes", data=data)
plt.show()