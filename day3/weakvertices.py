def solve(n, adj):
    """
    Adjacency lists of the given graph
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

    

