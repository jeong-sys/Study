# 5430, AC
'''
deaueue : 양쪽 끝에서 추가, 삭제가 가능한 선형 구조 형태의 자료구조
list사용시 시간초과 발생
'''

import sys
from collections import deque

t = int(input())

for i in range(t):

    p = sys.stdin.readline().rstrip()
    n = int(input())

    # 대괄호는 포함하면 안됨
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")

    # deaue생성
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0

    # 길이가 0인 경우는 초기화
    if n == 0:
        queue = []
        front = 0
        back = 0

    # 시간초과 안나게 해야함
    # 뒤집는 횟수가 홀수 번일때 뒤집도록 함(짝수번일경우 할 필요 없음)
    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
