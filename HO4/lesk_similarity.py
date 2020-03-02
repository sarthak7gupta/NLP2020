from itertools import product

from nltk.corpus import stopwords, wordnet as wn

sw = stopwords.words('english')


def defwords(syn):
	return set(filter(lambda x: x not in sw, syn.definition()))


def lesk_similarity(syn1, syn2):
	d1, d2 = defwords(syn1), defwords(syn2)
	return len(d1.intersection(d2)) / min(len(d1), len(d2))


def word_similarity(w1, w2):
	return max((lesk_similarity(i, j), i, j) for i, j in product(wn.synsets(w1), wn.synsets(w2)))


print(word_similarity('automobile', 'car'))
