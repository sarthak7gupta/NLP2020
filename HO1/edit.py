def editDistance(s1, s2, m, n):
	return n if not m else (m if not n else (editDistance(s1, s2, m - 1 , n - 1) if s1[m - 1] == s2[n - 1] else 1 + min(editDistance(s1, s2, m, n - 1), editDistance(s1, s2, m - 1, n), editDistance(s1, s2, m - 1, n - 1))))

def editDistanceDP(s1, s2):
	m = len(s1)
	n = len(s2)
	dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
	for i in range(m + 1):
		for j in range(n + 1):
			dp[i][j] = j if not i else (i if not j else (dp[i - 1][j - 1] if s1[i - 1] == s2[j - 1] else 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])))
	return dp[m][n]

s1 = 'intention'
s2 = 'execution'

# print(editDistance(s1, s2, len(s1), len(s2)))
print(editDistanceDP(s1, s2))

a = 'graffe'
b = 'graf', 'graB', 'grail', 'giraffe'

for s2 in b:
	print(editDistanceDP(a, s2))

