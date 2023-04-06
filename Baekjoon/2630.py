# 2로 계속 나눠주면서 비교하기
# 4분할 정복 : 4분할을 하여 한 사분면이 모두 같은 색일 때까지 분할하여 카운트하는 방법

N = int(input())
color = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0

def solution(x, y, n):
    global white, blue
    # 시작점 설정
    e_color = color[x][y]
    # 4분할
    for i in range(x, x+n):
        for j in range(y, y+n):
            if e_color != color[i][j]:
                solution(x, y, n // 2)
                solution(x+n//2, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n// 2, y+n//2, n//2)
                return
    if e_color == 1:
        blue += 1
    else:
        white += 1
    return

solution(0, 0, N)
print(white)
print(blue)