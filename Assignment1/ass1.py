#%%

from collections import Counter
import re

import matplotlib.pyplot as plt
import numpy as np
from nltk import pos_tag
from nltk.corpus import inaugural, stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from PIL import Image
from wordcloud import ImageColorGenerator, WordCloud

#%%

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))
speech_ids = inaugural.fileids()[-5:]

#%% Extract the raw text from the latest 5 speeches

a = raw_speeches = ' '.join(map(inaugural.raw, speech_ids))

print(a)

#%% Tokenize the raw text of these speeches into sentences

b = speeches_sentence_tokens = sent_tokenize(raw_speeches)

print(b)

#%% Tokenize the each sentence into words

c = speeches_word_tokens = word_tokenize(raw_speeches)

print(c)

#%% From the tokenized sentences, generate new sentence which is the sentence formed by removing the stop-words as well as stemming each word in the sentence.

speeches_filtered_words = filter(lambda x: x not in stop_words, speeches_word_tokens)

d = speeches_stemmed_filtered_words = ' '.join(map(ps.stem, speeches_filtered_words))

print(d)

#%% Tokenize the new sentence in D into words.

e = speeches_stemmed_filtered_word_tokens = word_tokenize(d)

print(e)

#%% Make separate Word Clouds of the words in C and words in E.

def wm(i, o):
	wordcloud_word_tokens = WordCloud(stopwords=stop_words, background_color="white", max_words=1000).generate(i)
	plt.figure(figsize=[7, 7])
	plt.imshow(wordcloud_word_tokens, interpolation="bilinear")
	plt.axis("off")
	plt.savefig(f"{o}.png", format="png")
	plt.show()
	return wordcloud_word_tokens

# def wm(i, o):
# 	mask = np.array(Image.open("usa.png"))
# 	wordcloud_word_tokens = WordCloud(stopwords=stop_words, background_color="white", max_words=1000, mask=mask).generate(i)
# 	image_colors = ImageColorGenerator(mask)
# 	plt.figure(figsize=[7, 7])
# 	plt.imshow(wordcloud_word_tokens.recolor(color_func=image_colors), interpolation="bilinear")
# 	plt.axis("off")
# 	plt.savefig(f"{o}.png", format="png")
# 	plt.show()
# 	return wordcloud_word_tokens

f = wm(' '.join(c), 'c'), wm(' '.join(e), 'e')

#%% Using POS tagging identify the frequency distribution of the different parts of speech of the words given in the text. (Use PennTree Tagset). Identify and represent the distribution via suitable visualization technique.

pos_tags = pos_tag(e)

h = freq_pos_tags = Counter(map(lambda x: x[1], pos_tags))

plt.bar(*zip(*freq_pos_tags.items()))
plt.show()

#%% Each sentence can be scored as the sum of frequencies of individual words (excluding stop words). Identify the top 5 sentences based on this score.

freq_word_tokens = Counter(speeches_word_tokens)

i = top_sentences_freq_score = sorted(speeches_sentence_tokens, key=lambda sentence: sum(freq_word_tokens[word] for word in sentence if word not in stop_words), reverse=True)[:5]

print(i)

#%% With the help of regular expressions, extract the words in E that have either numbers or other non-‐alphabetic characters.

r = re.compile(r'[^a-zA-Z]+')

j = non_alpha_containing_words = list(filter(r.search, e))

print(j)

#%%
