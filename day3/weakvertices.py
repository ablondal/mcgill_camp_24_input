def solve(n, adj_mat):
    pass


# Input. Don't Change. 
while True:
    n = int(input())
    if n == -1:
        break

    adj_mat = []
    for _ in range(n):
        adj_mat.append(
            list(map(int, input().split()))
        )
    
    solve(n, adj_mat)

    

