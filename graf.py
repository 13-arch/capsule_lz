# import libraries and packages 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

 
df = pd.read_csv('steam_players.csv') 


print(df) 

plt.title('количество игроков в стим')
df.hist() 
plt.show() 
