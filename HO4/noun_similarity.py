from nltk.corpus import wordnet as wn
from itertools import product


def get_similarity_score(pair):
	return max(i.path_similarity(j) or 0 for i, j in product(wn.synsets(pair[0]), wn.synsets(pair[1])) if i.pos() == j.pos())


def get_similarity_scores(pairs):
	return sorted(zip(map(get_similarity_score, pairs), pairs))


pairs = [('car', 'automobile'), ('gem', 'jewel'), ('journey', 'voyage'), ('boy', 'lad'), ('coast', 'shore'), ('asylum', 'madhouse'), ('magician', 'wizard'), ('midday', 'noon'), ('furnace', 'stove'), ('food', 'fruit'), ('bird', 'cock'), ('bird', 'crane'), ('tool', 'implement'), ('brother', 'monk'), ('lad', 'brother'), ('crane', 'implement'), ('journey', 'car'), ('monk', 'oracle'), ('cemetery', 'woodland'), ('food', 'rooster'), ('coast', 'hill'), ('forest', 'graveyard'), ('shore', 'woodland'), ('monk', 'slave'), ('coast', 'forest'), ('lad', 'wizard'), ('chord', 'smile'), ('glass', 'magician'), ('rooster', 'voyage'), ('noon', 'string')]


for score, pair in get_similarity_scores(pairs):
	print(f'{score:.2f}', *pair)
