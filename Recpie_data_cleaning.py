import pandas as pd
import random


dataframe = pd.read_csv('indian_food.csv')


sorted_df = dataframe.drop(columns=['state', 'region'])


recpies=pd.DataFrame(sorted_df)

recpies["quantity"]= random.randint(100, 1000, size=len(recpies))

recpies.to_csv('recpies.csv', index=False)