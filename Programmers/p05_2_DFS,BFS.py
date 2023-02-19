'''
n개의 정수가 있을때 순서 변경없이 부호만 변경하여 target넘버 만들기
return값 : target넘버를 만들 수 있는 경우의 수

예시 : solution([4, 1, 2, 1], 4) => 2
1) +4+1-2+1 = 4
2) +4-1+2-1 = 4

==> 던전깨기 문제랑 유사한듯? , DFS사용하는건
// 순열로도 풀 수 있을 것 같은데 한번 해보기(?)
'''
# 재귀를 이용한 DFS 
def solution(numbers, target): 
    answer = 0

    #  재귀
    def play(n, result):
        # 숫자 끝까지 더했을 때, 경우의 수 찾은 경우
        if n == len(numbers):
            # target 값 찾은 경우
            if result == target:
                # play에서 사용하는 answer이 밖에 있는 answer이라는 것을 표현해야함
                # local내 answer이 아님
                nonlocal answer
                answer += 1
            return
        # 숫자 더해주기
        else:
            play(n+1, result + numbers[n])
            play(n+1, result - numbers[n])
    play(0,0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))