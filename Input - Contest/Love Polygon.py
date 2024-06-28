n = int(input())

index = {}
cur = 0

adj = [[] for x in range(n)]

for i in range(n):
	s, t = input().split()

	si, ti = -1, -1

	if s not in index:
		index[s] = cur
		cur += 1

	if t not in index:
		index[t] = cur
		cur += 1

	si = index[s]
	ti = index[t]

	adj[si].append(ti)