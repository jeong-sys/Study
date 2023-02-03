from itertools import permutations, combinations

# 조합 사용하기
def solution(k, dungeons):
    answer = -1
    for case in permutations(dungeons, len(dungeons)):
        hp = k
        count = 0
        for require_hp, damage in case:
            if hp >= require_hp:
                hp -= damage
                count += 1
        if count > answer:
            answer = count
    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))