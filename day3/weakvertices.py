def solve(n, adj):
    """
    adj: Adjacency list of the given graph
    Vertices are numbered from 0 to n-1
    """
    pass


# Input. Don't Change. 
while True:
    n = int(input())
    if n == -1:
        break

    adj_mat = []
    adj = [[] for _ in range(n)]
    for i in range(n):
        row = list(map(int, input().split()))
        for j, val in enumerate(row):
            if val == 1:
                adj[i].append(j)

    
    solve(n, adj)

    

