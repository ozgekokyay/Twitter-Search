import pandas as pd
df = pd.read_csv('tweets.csv',usecols=[8,7,10,3,4,14,15,16],index_col=3)
df.to_csv(index=False)
df.to_csv('tweets_clean.csv')

