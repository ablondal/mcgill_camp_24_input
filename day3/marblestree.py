def solve(n, num_marbles, children):
    pass


# Input. Don't change.
while True:
    n = int(input())
    if n == 0:
        break

    num_marbles = []
    children = []
    for i in range(n):
        line = input().split()
        num_marbles.append(int(line[1]))

        num_children = int(line[2])
        chi = []
        for i in range(num_children):
            chi.append(int(line[3 + i]) - 1)

        children.append(chi)
    
    solve(n, num_marbles, children)



