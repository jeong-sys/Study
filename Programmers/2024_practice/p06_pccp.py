## PCCP 기출문제 2번, 석유 시추
## 배열에 따라 석유(land)가 덩어리로 있으며 석유관은 이를 거쳐 얻을 수 있는 최대 석유량을 계산하여라


def solution(land):
    
    height = len(land) - 1
    weight = len(land[0]) - 1
    
    # (0,1)~(0,4)에서 0번째 부분만 증가하여 석유관 위치 파악하기
    for m in range(weight):
        for n in range(height):
            pipe = land[n][m]
            if pipe == 1:
                ch_conn(n, m)
            
        
    answer = 0
    return answer

## 좌우 위아래 확인? 확인 과정에서 겹치는 덩어리들이 중복 체크 될 수 있는 위험
## 이진 탐색? 방향으로 풀 수 있을 것이라 생각했는데 BFS 방식으로 해결할 수 있음 --> 강의 수강 필요
def ch_conn(n, m):
    
    

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
## result 9