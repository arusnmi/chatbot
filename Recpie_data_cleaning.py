import pandas as pd
import random


dataframe = pd.read_csv('indian_food.csv')




recpies=pd.DataFrame(dataframe)


recpies.to_csv('recpies.csv', index=False)