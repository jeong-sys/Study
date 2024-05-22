def solution(routes):
    answer = 1
    '''
    람다 함수 = 일반 함수를 가볍게 만든 것
    < lambda 함수 만들기 >
    1) def 지우고 lambda 적기
    2) 함수 이름 지우기
    3) 소괄호 지우기
    4) 엔터 지우기
    5) return 지우기
    '''
    routes.sort(key=lambda route: route[1])
    camera = routes[0][1]
    '''
    그리디 알고리즘
    - 선택 할 수 있는 선택지 중에서 최선의 답
    - 범위가 많으므로 정렬이 필요함 (두개 걸린거)
    '''
    # routes 배열 반복
    for idx in range(1, len(routes)):
        start, end = routes[idx]
        if start > camera:
            camera = end
            answer += 1

    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
