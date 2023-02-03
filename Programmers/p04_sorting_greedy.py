def solution(routes):
    answer = 1
    routes.sort(key=lambda route: route[1])
    camera = routes[0][1]
    for idx in range(1, len(routes)):
        start, end = routes[idx]
        if start > camera:
            camera = end
            answer += 1
    # 그리디 알고리즘
    ## 선택할 수 있는 선택지 중에 최선의 답(?)
    ## 정렬(범위가 많기 때문에 정렬 필요)하고 두개 걸린거, 무조건 , 마지막 걸린거 (?)
    ## lambda

    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
