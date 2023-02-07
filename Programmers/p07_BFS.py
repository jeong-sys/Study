'''
Tip !
 메소드가 기억나지 않을때 print(dir(deque))사용하기
'''

from collections import deque
# 끝 지점에 있는 값에 접근하기 최적화 되어있다.

def solution(s, e):
    answer = 0
    to_visits = [s]
    '''
    # 방문 체크
    ## 이미 있었던 숫자는 다시 경우의 수 따질 필요가 없다.
    ## 수직선 상의 좌표는 1부터 10,000까지이다.
    '''
    visited = [False for _ in range(10001)]

    # +1, -1, +5 // 반복 - e가 나올 때까지
    while to_visits:
        # 목적지에 남아있는 좌표 개수로 반복
        for _ in range(len(to_visits)):
            '''
            # 시간 초과 남
            ## 리스트는 인덱스로 접근하므로 맨 앞 빼주면, 그 뒤에 인덱스를 모두 바꿔줘야함.
            # now = to_visits.pop(0)
            => 따라서 뒤에를 빼면, 시간 초과가 안 날 수 있다. = dequeue
            
            정렬된 리스트에 append하면 다시 정렬하는 것을 반복해야함 -> 비 효율적
            => 넣는 순간 정렬되는 것 == heap
            '''
            # Double-Ended-Queue => deque
            now = to_visits.popleft()

            # 방문 체크
            visited[now] = True
            # 찾았다면 return
            if now == e:
                return answer
            # 못 찾았다면, 다음 목적지를 추가해야 함.
            for nxt in [now-1, now-1, now+5]:
                # 다음 목적지들의 조건 ==> 방문 안했어야 함 / 좌표 범위 내부
                if 0 < nxt <= 10000 and visited[nxt] == False:
                # 순서 중요함, 에러 날 수 있음 // 아래와 같은 순서의 반복문이면 안됨
                # if visited[nxt] == False and 0 < nxt <= 10000:
                    to_visits.append(nxt)
        # answer +1 // 반복문 끝났을때, 한번의 점프가 끝났을 때 answer 하나 추가함
        answer += 1
    return answer

print(solution(5, 14))
print(solution(8, 3))

'''
내 아이디어)
v1 = 0, v2 = 0, v3 = 0
# # +1, -1, +5 // 반복 증가함
# ## 시작 값도 증가한다
# while s == e:
#     v1 = s+1
#     v2 = s-1
#     v3 = s+5 ==> 이러한 방법이 아닌 위의 방법 처럼 반복문 내에 목적지 찾지 못하면 추가하기
'''