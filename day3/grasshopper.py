def solve(R, C, G_R, G_C, L_R, L_C):
    pass


# Input. Don't change
import sys

input_data = sys.stdin.read().strip()
lines = input_data.split('\n')

for line in lines:
    line = line.strip()
    if len(line) == 0:
        break
    
    R, C, G_R, G_C, L_R, L_C = list(map(int, line.split()))

    solve(R, C, G_R, G_C, L_R, L_C)
