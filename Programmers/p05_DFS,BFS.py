from itertools import permutations
###  재귀?

def solution(numbers, target):
    answer = 0

    for p in permutations(numbers, len(numbers)):
        for m in permutations(numbers*(-1), len(numbers)):
            sum = 0
            sum += m 

    if sum == target:
        answer += 1

    return answer

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))  