# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램
# 순서대로 증가하는 배열을 나타내는거?
# 앞의 것과 비교하면서 크면 증가하는 걸로 넣음

# LIS라는 DP문제임
'''
DP(동적 계획법) 사용 이유 : 일반적인 재귀를 단순히 사용 시 동일한 작은 문제들이 여러 번 반복되어 비효율적인 계산

DP 사용 조건
1) Overlapping Subproblems (겹치는 부분 문제) : 동일한 작은 문제들 반복
2) Optimal Substructure (최적 부분 구조) : 부분 문제의 최적 결과 값을 사용해 전체 문제의 최적 결과를 낼 수 있다.

DP 사용법
1) DP로 풀 수 있는 문제인지 파악
2) 문제의 변수 파악(state)
3) 변수 간 관계식 만들기(점화식)
4) 메모하기(Memoization) 변수의 값에 따른 결과를 저장해야한다.
5) 기저 상태 파악 하기
6) 구현하기 - (1)반복문 사용 (2)재귀 사용

구현 방법
1) Bottom-Up 방식
    - 아래에서부터 계산을 수행하고 누적시켜서 전체 큰 문제를 해결하는 방식
    - dp[0]이 기저 상태이고 dp[n]을 목표 상태라 했을때 dp[0]부터 dp[n]까지 값을 전이시켜 재활용
2) Top-Down 방식
    - dp[n]값을 찾기 위해 위에서부터 바로 호출을 시작하여 dp[0]의 상태까지 내려간 다음 해당 결과 값을 재귀를 통해 전이시켜 재활용

'''

# # 피보나치 예시
# memoization = [0] * 100
# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     if memoization[x] != 0:
#         return memoization[x]
#     memoization[x] = fibo(x-1) + fibo(x-2)
#     return memoization[x]
# print(fibo(6))


N = int(input())
length = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if length[i] > length[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))