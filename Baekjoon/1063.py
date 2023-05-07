# 킹

loc_king, loc_rock, N = map(int, input().split())
loc_move = []

for _ in range(N):
    loc = input()
    loc_move.append(loc)

R = [0, 1]
L = [0, -1]
B = [1, 0]
T = [-1, 0]
RT = [-1, 1]
LT = [-1, -1]
RB = [1, 1]
LB = [1, -1]

