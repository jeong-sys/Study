# 삼각 달팽이(Level 2)
## 정수 n이 매개변수로 주어질때, 밑변의 높이가 n인 삼각형
## 맨 위부터 반시계 방향으로 달팽이 채우기를 한 후, 첫 행부터 마지막 행까지 모두 합친 새로운 배열 구하기

def soulution(n):
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    snail = [[0] * i for i in range(1, n + 1)]
    x = y = angle = 0
    cnt = 1
    size = (n+1) * n // 2

    while cnt <= size:
        snail[y][x] = cnt
        ny = y + dy[angle]
        nx = x + dx[angle]
        cnt += 1

        if 0 <= ny < n and 0 <= nx <= ny and snail[ny][nx] == 0:
            y, x = ny, nx
        else:
            angle = (angle + 1) % 3

            y += dy[angle]
            x += dx[angle]

    return [i for j in snail for i in j]

print(soulution(4))
