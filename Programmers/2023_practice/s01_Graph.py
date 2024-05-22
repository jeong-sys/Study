# graph.py
graph = [
    [],             # 0 (버림)
    [2, 3],         # 1
    [1, 3, 5],      # 2
    [1, 2, 5, 4],   # 3
    [3],            # 4
    [2, 3]          # 5
]

'''
D(뒤)FS 탐색
- stack을 사용하여 뒤에서 빼준다.
- 방문한 정점들을 스택에 저장하였다가 다시 꺼내어 작업
'''
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

'''
BFS 탐색
- 리스트의 앞의 값을 빼준다
'''
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

'''
DFS 구현 - 재귀
- stack 자료구조를 사용하는 DFS만 재귀로 가능하다
- 반복문이 속도도 빠르고 효율적이지만, 재귀적인 사고가 가능한가 확인하기 위해 재귀를 사용한다.
'''
s = 1
v = 5
visited = [False for _ in range(v + 1)]

def dfs_r(now):
    visited[now] = True
    for nxt in graph[now]:
        if not visited[nxt]:
            dfs_r(nxt)

dfs_r(1)
