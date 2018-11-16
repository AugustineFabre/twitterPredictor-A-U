# twitterPredictor-A-U
twitter_connection_setup.py: for autification and connection with twitter
collect_candidate_actuality_tweets_teacher: collect tweets with api search
(hashtag_candidate_0,hashtag_candidate_1,keywords_candidate_0,keywords_candidate_1: hashtags and keywords of candidates for api search
(tweet_collect_whole: combine all the keywords and hastags in a list
collect_candidate_actuality_tweets: collect tweets with api search
collect_avec_streamfilter: collect tweets with api stream and filter
collect_candidate_tweet_activity: collect retweets of candidates' tweets)
store_tweets: transform the resulting tweets of api search to the form json
(tweets_candidat_0.json, tweets_candidat_1.json: the resulted json file)
to_dataframe: transform the json file to form pandas
(twitter_search, to_dataframe, test_transform_to_data_frame: test for the file to_dataframe)
most_retweet_and_like: search the tweet with the most retweets/likes
visualisation_retweet_and_like: visualier the result of most_retweet_and_like in graghs
text_blob: correct the tweets' text in the result of api search in collect_candidate_actuality_tweets_teacher and transform them into a list of useful words
pos_neu_neg: get the number of positif/neutre/negatif tweets
histogramme_tweet: visualisation of pos_neu_neg for every candidate

we have finished the fonctionalité 1~10 without bug, the final graph is in the form .pdf

we tried to do the fonctionalité 11 and 13
