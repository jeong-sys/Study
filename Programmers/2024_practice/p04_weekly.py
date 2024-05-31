# 위클리 챌린지, 교점에 별 만들기
## 교점을 구하고 최소한의 범위로 표현하기
## 교점 구하는 공식(a1,b1,c1)(a2,b2,c2)
##   - x : (b1*c2 - c1*b2)/(a1*b2 - b1*a2)
##   - y : (c1*a2 - a1*c2)/(a1*b2 - b1*a2)
from itertools import combinations

def calculation(eq1, eq2):
    a1, b1, c1 = eq1
    a2, b2, c2 = eq2
    
    # 기울기가 같은 경우
    if a1*b2 == b1*a2:
        return 
    
    x = (b1*c2 - c1*b2)/(a1*b2 - b1*a2)
    y = (c1*a2 - a1*c2)/(a1*b2 - b1*a2)
    
    # 정수인 경우에 반환
    if x == int(x) and y == int(y):
        return [int(x), int(y)]


def solution(line):
    
    points = []
    
    # 모든 점 교점확인
    for eq1, eq2 in combinations(line, 2):
        point = calculation(eq1, eq2)
        if point: points.append(point)
    
    # 그림 시작점, 마지막점 찾기
    w1, w2 = min(points, key = lambda x: x[0])[0], max(points, key = lambda x: x[0])[0] + 1
    h1, h2 = min(points, key = lambda x: x[1])[1], max(points, key = lambda x: x[1])[1] + 1
        
    # 최소한 크기 배열 생성
    answer = [['.'] * (w2-w1) for _ in range((h2 - h1))]
    
    # * 변환
    for x, y in points:
        answer[y-h1][x-w1] = '*'
    
    answer.reverse()
    
    return [''.join(a) for a in answer] 


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
# ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"]

## python에서 라이브러리를 불러오는것에 취약하다
## 특히 이번 풀이에서 모두 for문으로 돌리려고 해서 더 복잡해졌다. 이럴때 함수를 사용해서 구분하는 연습이 필요한 것 같다