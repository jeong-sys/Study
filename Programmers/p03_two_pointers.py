def solution(gems):
    # 현재 구간
    answer = []

    start_idx = 0
    # 최소한 사는 개수(초기값 => 최대)
    minimum = len(gems)
    # 사야하는 보석의 종류의 개수
    uinq_count = len(set(gems))
    # 사야하는 구간의 시작과 끝(idx+1)
    answer = [1, len(gems)]
    # 현재까지의 구매 리스트 {'dia':1, 'ruby':1}
    buy_list = {}
    '''
    # 시작(s) 값 고정, e값 1씩 증가
    ## 보석 4개 다 있을 때까지
    ## 저장

    # e 고정, s 값 1증가
    ## 모든 보석 있으면 계속 증가
    ## 보석 없으면 중지
    ### 여기서 보석 다 더한 값이 처음보다 작으면 계속 저장
    '''
    for end_idx in range(len(gems)):
        # 현재의 구간에서 마지막 gem을 저장해주고 buy_list 갱신
        # 처음 사는 건지, 기존에 산 적이 있는지 구분 필요

        # end_idx 전진하면서 모든 보석을 샀는지 확인
        # 만약 다 샀다면, 지금까지 산 보석 개수 저장 후 , start_idx 전진
        # 전진해도 모든 보석 구간 안에 있으면,
        # 진행하다 하나라도 0이 되면, end_idx 전진

# [3, 7]
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# # [1, 3]
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
# # [1, 1]
# print(solution(["XYZ", "XYZ", "XYZ"]))
# # [1, 5]
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

# 시간 초과 - 이중 for 문
# start 정하고 end하나씩 늘려서 모든 종류 보석 있을때 몇개 사는지 계상
# start 하나씩 늘리고 다시 end 하나 씩 늘려서 ~~