# 11561, 징검다리
# 이거 너무 어렵다 ,, 꼬인느낌

'''

등차수열 / 이분탐색
# 초기값이 1이고 차이가 1인 등차수열의 합 = 징검다리 총 수
## 등차수열 합 < 징검다리 총 수
    => 마지막 m번째 돌 넓게 점프

등차 수열 공식
# n(n+1)/2

'''

test_case = int(input())

for i in range(test_case):
    n_time = int(input())

# 반복
for n in range(test_case):

# 진짜 시작
# 입력값 : n
    start = 0
    end = n

