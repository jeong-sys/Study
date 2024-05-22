# p07_BFS 시간 초과에 대한 해답

from collections import deque

def solution(s, e):
    visited = [0] * 10001
    to_visits = deque()
    initial_tries = 1

    '''최소 점프를 위해 이미 5칸 이상 벌어져 있는 경우 최대한 5칸씩 오른쪽으로 보내기'''
    if e >= s + 5:
        fast_move = (e - s) // 5
        initial_tries += fast_move
        to_visits.append((new_start, initial_tries))
    else:
        to_visits.append((s, initial_tries))

    while to_visits:
        current, tries = to_visits.popleft()  # 현재 위치와 to_visits에서 뽑고!
        visited[current] = tries  # 방문 체크가 최초 되는 tries 가 중요함! (이게 그냥 최초 일거라서)
        if e == current:  # 현재 위치가 찾는 위치라면?
            return tries - 1  # 횟수 조정 해서 return
        elif e < current and not visited[current-1]:  # 현재 위치가 더 큰 경우? 왼쪽으로 1칸만 가능
            to_visits.append((current-1, tries+1))
        elif e > current:  # 현재 위치가 작은 경우는, 일단 5로 가보고, 1로 가보고 둘다 to_visits에 넣음
            if not visited[current+5]:
                to_visits.append((current+5, tries+1))
            if not visited[current+1]:
                to_visits.append((current+1, tries+1))