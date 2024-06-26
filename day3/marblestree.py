def solve(n, num_marbles, adj):
    pass


# Input. Don't change.
while True:
    n = int(input())
    if n == 0:
        break

    num_marbles = []
    adj = [[] for _ in range(n)]
    for i in range(n):
        line = input().split()
        num_marbles.append(int(line[1]))

        num_neighs = int(line[2])
        neighs = list(map(int, line[3:]))
        for nei in neighs:
            nei -= 1
            adj[nei].append(i)
            adj[i].append(nei)

    
    solve(n, num_marbles, adj)



