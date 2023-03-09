def solution(relation):

    # 처음에는 무작정 이중 for 문으로 돌리려고 시도
    # # [0][0], [1][0] ... 비교 해서 다르면 숫자 증가 ,, 모든 배열
    # for i in range(len(relation)) - 1:
    #     for j in range(len(relation)):
    #         if relation[j][i] not in relation:
    #             answer += 1 # (?) 안되는데
    #

    f_answer = 0

    # 학번, 이름, 과목, 학년에 맞게 리스트 분리.
    number, name, subject, grade = relation.split

    number = number.set()
    name = name.set()
    subject = subject.set()
    grade = subject.set()

    # 재귀함수 써서 중복 된것 제거한 뒤에 겹치는지 안겹치는지 확인.
    def cal(n):
        answer = 0
        if len(n) < len(relation):
            pass
        else:
            answer += 1

            # 삭제 후 진행을 여기에서 쓰면 ?
            if answer == 0:
                # (?)

        return answer

    # 나머지 것들도 재귀 함수를 사용하여 동일 하게 하려고 했지만 위에서 set을 진행하여 사용할 수가 없음.
    # set 해버려서 쓸 수가 없음.
    # 해당 부분 삭제후 진행하려고 함.
    def cal_2(m):
        answer2 = 0

        if m == 0:

            # (?)

        else:
            pass

        return answer2

    f_answer1 = cal(number) + cal(name) + cal(subject) + cal(grade)
    f_answer2 = cal_2(cal(number)) + cal_2(cal(name)) + cal_2(cal(subject)) + cal_2(cal(grade))

    f_answer = f_answer1 + f_answer2

    return f_answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
          ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
# 출력 : 2