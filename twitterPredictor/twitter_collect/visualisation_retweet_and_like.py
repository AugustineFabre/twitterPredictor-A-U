import pandas as pd
import matplotlib.pyplot as plt
from tweet_collect.to_dataframe import *
data_pd_0, data_pd_1 = myfonc()


plt.subplot(121)

tfav = pd.Series(data=data_pd_0['likes'].values, index=data_pd_0['Date'])
tret = pd.Series(data=data_pd_0['RTs'].values, index=data_pd_0['Date'])

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)
plt . title ('Retweets and likes of Macron', fontsize =18)

#plt.show()



plt.subplot(122)
tfav1 = pd.Series(data=data_pd_1['likes'].values, index=data_pd_1['Date'])
tret1 = pd.Series(data=data_pd_1['RTs'].values, index=data_pd_1['Date'])

# Likes vs retweets visualization:
tfav1.plot(figsize=(16,4), label="likes", legend=True)
tret1.plot(figsize=(16,4), label="Retweets", legend=True)

#plt.show()


plt.show()
