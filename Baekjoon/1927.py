# 최소 힙
import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())

    # x가 0인경우 가장 작은 값 출력
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        # 배열이 비어 있으면 0 출력
        else:
            print(0)
    # x 가 0이 아닌경우
    else:
        heapq.heappush(heap, x)

