from nltk.corpus import wordnet
from statistics import mean

def average_polysemy(pos):
    words=set(map(lambda x: x.name().split('.')[0], wordnet.all_synsets(pos)))
    return mean(map(lambda x: len(wordnet.synsets(x)), words))

print('Nouns: ', average_polysemy('n'))
print('Verbs: ', average_polysemy('v'))
print('Adjectives: ', average_polysemy('a'))
print('Adverbs: ', average_polysemy('r'))