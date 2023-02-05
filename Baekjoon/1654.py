'''
1654, 랜선 자르기
영식이가 모두 다른 길이를 가진 k 개의 랜선을 같은 길이로 n 개 만들려고함
여기서, 랜선의 최대 길이는?

예시 ) 
4개(802, 743, 457, 539)의 랜선을 11개로 만들 수 있음. 
(200cm 로 자름)

!! 자를때는 정수길이만큼 자른다

-> 이진탐색 문제라는데 그렇게 생각하는게 어려웠음
==> 랜선의 길이를 움직여서 랜선 개수를 만족하는지 확인
'''
# 입력
k, n = input().split()
line_list = []

for i in range(int(k)):
    line_list.append(int(input()))
###

start = 1
end = max(line_list)

# 1부터 가장 긴 랜선까지 길이
while start <= end:
    # 중간 위치
    mid = (start + end)//2
    # 랜선의 수
    line = 0
    # 랜선을 자른 수
    for i in range(int(k)):
        line += line_list[i] // mid
    # 랜선 자른 수가 목표 값보다 큰 경우
    if line >= int(n):
        # 랜선 최소 길이 중간값 + 1
        start = mid + 1
    else:
        # 랜선 최소 길이 중간값 - 1
        end = mid - 1

print(end)


