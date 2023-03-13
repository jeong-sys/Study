from itertools import combinations
# combination 사용,,**
# combination을 사용한 모든 인덱스 조합을 구해야함

'''
처음에는 이중 for문, 재귀 함수를 통해서 구하는 방법을 생각했었음.
유일성까지는 구했는데 최소성을 구하는 것에서 많이 헤맴
issubset을 사용한 부분집합 접근법은 꼭 기억해둬야할 것 같음
'''

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    # 모든 조합 구해주기
    com = []
    for i in range(1, col + 1):
        com.extend(combinations(range(col), i))

    only = []
    for i in com:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        # 유일성 구하기 : 중복성 확인해서 relation 길이랑 일치하는지 확인해야함
        if len(set(tmp)) == row:
            put = True
            # 최소성 구하기 : 유일성 검사하고 부분집합 인지 찾는다
            for x in only:
                if set(x).issubset(set(i)):  # 최소성
                    put = False
                    break

            if put:
                only.append(i)

    return len(only)