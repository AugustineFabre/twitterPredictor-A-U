import numpy as np
from tweet_collect.to_dataframe import *
data_pd_0, data_pd_1 = myfonc()

# Max RTs of Macron:
rt_max  = np.max(data_pd_0['RTs'])
rt  = data_pd_0[data_pd_0.RTs == rt_max].index[0]


print("The tweet with more retweets of Macron is: \n{}".format(data_pd_0['tweet_textual_content'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data_pd_0['len'][rt]))


# Max RTs of Marie Le Pen:
rt_max  = np.max(data_pd_1['RTs'])
rt  = data_pd_1[data_pd_1.RTs == rt_max].index[0]

print("The tweet with more retweets of Marie Le Pen is: \n{}".format(data_pd_1['tweet_textual_content'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data_pd_1['len'][rt])

#Max likes of Macron:
like_max  = np.max(data_pd_0['likes'])
like  = data_pd_0[data_pd_0.likes == like_max].index[0]


print("The tweet with more likes of Macron is: \n{}".format(data_pd_0['tweet_textual_content'][like]))
print("Number of likes: {}".format(like_max))
print("{} characters.\n".format(data_pd_0['len'][like]))

#Max likes of Marie Le Pen:
like_max  = np.max(data_pd_1['likes'])
like  = data_pd_1[data_pd_1.likes == like_max].index[0]


print("The tweet with more likes of Marie Le Pen is: \n{}".format(data_pd_1['tweet_textual_content'][like]))
print("Number of likes: {}".format(like_max))
print("{} characters.\n".format(data_pd_1['len'][like]))
