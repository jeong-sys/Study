# 11561, 징검다리
# 이거 너무 어렵다 ,, 꼬인느낌
'''
등차수열 / 이분탐색
# 초기값이 1이고 차이가 1인 등차수열의 합 = 징검다리 총 수
## 등차수열 합 < 징검다리 총 수
    => 마지막 m번째 돌 넓게 점프

등차 수열 공식
# n(n+1)/2

이분 탐색 쓰임은 알겠지만 그로 인한 응용 연습 더 필요 
'''
import sys
from math import sqrt

# 근의 공식
mx = int(-1 + sqrt(1 - 4*(-2*int(1e16)))//2) + 1 
# 테스트 케이스의 수
t = int(sys.stdin.readline())

while t:
    t -= 1
    n = int(sys.stdin.readline())
    s, e, ans = 0, mx, 0
    while s < e:
        mid = (s+e)//2
        # 등차수열 합 < 징검다리 총 수
        if (mid + 1) * mid//2 <= n:
            ans = mid
            s = mid+1
        else:
            e = mid
    print(ans)

    
