import pandas as pd 
import numpy as np

# drink 데이터
drink = pd.read_csv("drink.csv")
#print(drink.head())
#print(drink.info())
"""
1. 도수 계산
"""
drink_freq = drink[drink['Attend'] == 1]['Name'].value_counts()


print("도수분포표")
print(drink_freq)