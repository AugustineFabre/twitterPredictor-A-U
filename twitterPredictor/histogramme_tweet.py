import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#从POS_NEU_NEG得到6个tweeets【】
from tweet_analysis.pos_neu_neg import *
tweets_positif_0,tweets_negatif_0,tweets_neutre_0,tweets_positif_1,tweets_negatif_1,tweets_neutre_1=positivite()
posi_macron = len(tweets_positif_0)*100/len(data_pd_0['tweet_textual_content'])
neut_macron = len(tweets_neutre_0)*100/len(data_pd_0['tweet_textual_content'])
nega_macron = len(tweets_neutre_0)*100/len(data_pd_0['tweet_textual_content'])

posi_lepen = len(tweets_positif_1)*100/len(data_pd_1['tweet_textual_content'])
neut_lepen = len(tweets_neutre_1)*100/len(data_pd_1['tweet_textual_content'])
nega_lepen = len(tweets_negatif_1)*100/len(data_pd_1['tweet_textual_content'])


import csv
# 文件头，一般就是数据名
fileHeader = [u"candidate_name", u"positivite",u"valeur"]
# 假设我们要写入的是以下两行数据
line1 = ["Marine Le Pen", "positif", posi_lepen]
line2 = ["Marine Le Pen", "neutre", neut_lepen]
line3 = ["Marine Le Pen", "negatif", nega_lepen]
line4 = ["Emmanuel Macron", "positif", posi_macron]
line5 = ["Emmanuel Macron", "neutre", neut_macron]
line6 = ["Emmanuel Macron", "negatif", nega_macron]
# 写入数据
csvFile = open("instance.csv", "w")
writer = csv.writer(csvFile)

# 写入的内容都是以列表的形式传入函数
writer.writerow(fileHeader)
writer.writerow(line1)
writer.writerow(line2)
writer.writerow(line3)
writer.writerow(line4)
writer.writerow(line5)
writer.writerow(line6)

csvFile.close()



sns.set(style="whitegrid")

# Load the example Titanic dataset
#datatweet = sns.load_dataset("instance")

# Load the data
datatweet = pd.read_csv("/Users/apple/PycharmProjects/twitterPredictor1/tweet_analysis/instance.csv")


# Draw a nested barplot to show degree for opinion and candidates
g = sns.catplot(x="positivite", y="valeur", hue="candidate_name", data=datatweet,height=6, kind="bar", palette="muted")
g.despine(left=True)
g.set_ylabels("degree of opinion")

plt.show()

