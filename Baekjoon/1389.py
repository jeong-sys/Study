'''
1389번
유저 존재할때 최소 연결 단계
'''
# 모든 경우의 수 방문
# bfs
import sys
from collections import deque

# 입력
n,m = map(int,sys.stdin.readline().split())

# 2차원 그래프
graph = [[] for _ in range(n+1)]
# 친구 관계 : a-b = b-a 
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# bfs 탐색
def play(graph,s):
    num = [0] * (n+1)
    # 시작
    visited[s] = 1
    q = deque()
    q.append(s)
    # 방문 체크
    while q:
        a = q.popleft()
        # 친구 관계 확인
        for j in graph[a]:
            # 탐색하지 않은 친구 탐색
            if visited[j] == 0:
                num[j] = num[a] + 1
                q.append(j)
                visited[j] = 1
    # 탐색하면서 걸린 횟수
    return sum(num)

# 케빈 베이컨 수
result = []

# 모든 사람 탐색
for k in range(1, n+1):
    visited = [0] * (n + 1)
    result.append(play(graph,k))

# 가장 작은 케빈 베이컨 수를 가진 사람의 인덱스 + 1   
print(result.index(min(result))+1)
