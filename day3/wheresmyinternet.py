def dfs(node, adj, visited):
    pass


# Input. Don't change.
import sys
sys.setrecursionlimit(300000)


n, m = list(map(int, input().split()))
edge_list = []
for _ in range(m):
    edge_list.append(
        list(map(int, input().split()))
    )

solve(n, m, edge_list)


