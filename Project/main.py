# %%
import pandas as pd

# %%
# scrapy crawl TweetScraper -a query="string" -a lang=en -a top_tweet=True
# from os import listdir
# import json

# datadir = 'TweetScraper/Data/tweet'
# files = listdir(datadir)

# df = []

# for f in files:
# 	with open(f'{datadir}/{f}') as fo:
# 		try:
# 			js = json.loads(fo.read())
# 		except json.decoder.JSONDecodeError as er:
# 			print(f, er)
# 		df.append(js['text'])

# df = pd.DataFrame(df, columns=['text'])

# df.to_csv('tweets.csv')

tweets = pd.read_csv('tweets.csv')

print(tweets)

# %%
"""
Detect overall sentiment, first half sentiment, second half sentiment, emoji sentiment. Compare
"""

# %%
"""
input
preprocessing
cleaning, punct, hasta, noice, non english, stop word
classification - 2 + hybrid
collaborative
ensemble
sequence to sequence
feature selection passed to another model

ppt
title, name, srn
literature review

"""
