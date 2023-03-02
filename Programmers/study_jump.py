# 점프와 순간 이동
def solution(n):
    ans = 0
    ## 이거 이진 탐색인가 ?

    # 반복
    while n == 1:
        if n % 2 == 0:
            n = n/2
            ans += 1

        else:
            n = n/2 - 1
            ans += 1

    return ans

print(solution(5)) #2
print(solution(6)) #2