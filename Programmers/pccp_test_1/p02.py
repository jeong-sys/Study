# 순열 맞으니까 순열 공부 한번 해보기
from itertools import permutations

def solution(ability):
    # 종목 수
    play_num = len(ability[0])
    answer = 0

    # 순열로 종목 수만큼 ability 생성 5P3
    ## score 한번 나오면 그 다음, for문 돌기
    for r in permutations(ability, play_num):
        # 한번 돌 때마다 점수 0으로 초기화
        score = 0
        # 3개의 리스트에서, 하나의 리스트당 차례로 인덱스(각 다른 인덱스, 다른 종목) 붙이기
        for idx, stat in enumerate(r):
            score += stat[idx]

        # 최대 값 찾기   
        if answer < score:
            answer = score

    return answer

print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
print(solution([[20, 30], [30, 20], [20, 30]]))


## 메소드 판별하기, 프린트하기
from itertools import *
print(dir())