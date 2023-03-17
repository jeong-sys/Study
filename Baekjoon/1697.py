# 숨바꼭질
# BFS, DFS ,, 그래프

x, k = map(int, input().split())

sum = 0
ch = 0

print(17 % 2)

while k // 2 >= x:
    k = k // 2
    sum += 1
    print(sum)

if k % 2 != 0:
    ch = k % 2
sum = sum + ch

print(sum)

