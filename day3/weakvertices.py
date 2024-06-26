def solve(n, adj_mat):
    """
    adj_mat: The adjacency matrix, as given in the question. It is stored in a 2D list, for example,
    [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    """
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

    

