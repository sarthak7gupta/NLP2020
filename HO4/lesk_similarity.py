from nltk.corpus import wordnet
from nltk.corpus import stopwords
from operator import itemgetter

def lesk_similarity(syn1,syn2):
    def1words=set(x for x in syn1.definition() if x not in stopwords.words('english'))
    def2words=set(x for x in syn2.definition() if x not in stopwords.words('english'))
    return len(def1words.intersection(def2words))/min(len(def1words),len(def2words))

def word_similarity(word1,word2):
    return max((lesk_similarity(i, j), i, j) for i in wordnet.synsets(word1) for j in wordnet.synsets(word2))

print(word_similarity('automobile', 'car'))