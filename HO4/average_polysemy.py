from nltk.corpus import wordnet
from statistics import mean


def average_polysemy(pos):
	words = set(map(lambda x: x.name().split('.')[0], wordnet.all_synsets(pos)))
	return mean(map(lambda x: len(wordnet.synsets(x)), words))


a = {'Nouns': 'n', 'Verbs': 'v', 'Adjectives': 'a', 'Adverbs': 'r'}

for postag, pos in a.items():
  print(f'{postag}: {average_polysemy(pos):.2f}')
