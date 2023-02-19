# 상하좌우로 이동 가능
# bfs 탐색
from collections import deque

def solution(maps):
    answer = 0
    # 상하좌우확인 리스트
    dx = [-1, 1, 0, 0] # 행 이동
    dy = [0, 0, -1, 1] # 열 이동

    def play(x, y):
        queue = deque()
        queue.append((x, y))
        # queue가 빌 때까지 반복(선입선출)
        while queue:
            x, y = queue.popleft()
            # 상하좌우 칸 확인하기(4가지 방향)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 맵 넘어가면 무시
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): 
                    continue
                # 벽 무시하기
                if maps[nx][ny] == 0:  
                    continue
                # 처음 방문 칸, 거리계산하고 상하좌우 확인
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny)) 

        distance = maps[len(maps)-1][len(maps[0])-1]
        # 제일 오른쪽 아래 칸 까지의 거리 반환
        return distance

    answer = play(0, 0)
    return -1 if answer == 1 else answer    # 도착 못하면 -1