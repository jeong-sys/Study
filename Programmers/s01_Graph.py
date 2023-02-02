# graph.py

graph = [
    [],             # 0 (버림)
    [2, 3],         # 1
    [1, 3, 5],      # 2
    [1, 2, 5, 4],   # 3
    [3],            # 4
    [2, 3]          # 5
]

# D(뒤)FS 탐색 - 뒤에서 빼준다 / 자료구조 - stack 사용
## 리스트의 위의 값을 뺀다
def dfs():
    s = 1

    # 그래프에서 정점의 개수
    v = 5

    # 1. 목적지
    to_visits = [s]

    # 2. 방문 체크
    visited = [False for _ in range(v+1)]

    ## to_visits의 요소가 하나라도 있으면 반복
    # while len(to_visits) != 0:
    while to_visits:
        # 리스트 뒤의 값을 빼서, 방문함
        now = to_visits.pop()
        # 현재 위치를 방문하지 않은 경우에만,
        if not visited[now]:
            # 방문 체크
            visited[now] = True
            print(now)
            # 다음 목적지 추가
            to_visits += graph[now]
dfs()

# BFS 탐색
## 리스트의 앞의 값을 뺀다
def bfs():
    s = 1

    # 그래프에서 정점의 개수
    v = 5

    # 1. 목적지
    to_visits = [s]

    # 2. 방문 체크
    visited = [False for _ in range(v + 1)]

    ## to_visits의 요소가 하나라도 있으면 반복
    # while len(to_visits) != 0:
    while to_visits:
        # 리스트 뒤의 값을 빼서, 방문함
        now = to_visits.pop(0)
        # 현재 위치를 방문하지 않은 경우에만,
        if not visited[now]:
            # 방문 체크
            visited[now] = True
            print(now)
            # 다음 목적지 추가
            to_visits += graph[now]
print('\n')
bfs()

# DFS 재귀로 할 수 있음
## DFS 가 stack 이여서 DFS만 재귀로 가능하다
## 반복문이 속도도 빠르고 효율적이지만, 재귀적인 사고를 할 수 있는지 보이기 위해 재귀 사용한다.
s = 1
v = 5
visited = [False for _ in range(v + 1)]

def dfs_r(now):
    visited[now] = True
    for nxt in graph[now]:
        if not visited[nxt]:
            dfs_r(nxt)

dfs_r(1)
