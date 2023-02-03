
# 순열 맞으니까 순열 공부 한번 해보기

def solution(ability):

    def play(i, j):
        students_num = len(ability)
        play_num = len(ability[0])

        for i in range(students_num):
            for j in range(play_num):
                ability[i][j]


    answer = 0
    return answer

print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
print(solution([[20, 30], [30, 20], [20, 30]]))