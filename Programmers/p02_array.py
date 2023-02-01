def solution(fees, records):
    answer = []

    parking_info = {}
    time_info = {}
    # 주차요금 계산 함수 // 계산 반복
    ## get_fee(131) ==> 15400
    def get_fee(total_min):
        basic_time, basic_fee, unit_time, unit_fee = fees
        # 추가 청구되는 시간
        charge_time = total_min - basic_time
        # 올림
        import math
        math.ceil(charge_time / unit_time) * unit_fee

        return basic_fee + charge_time

    #3개로 나누기 리스트 분류 가능
    for record in records:
        time, car, inout = record.split()

        # car 번호의 차가 처음 들어 왔다면,
        if not time_info.get(car):
            # 주차시간 0
            time_info[car] = 0
            # 주차장 여부 True
            parking_info[car] = False

    '''list.split 할때 여러 개 변수 놓기'''
    h, m = map(int, time.split(':'))
    if inout == 'IN':
        time_info[car] -= h * 60 + m
        parking_info[car] = True
    else:
        time_info[car] += h * 60 + m
        parking_info[car] = False

    # 23:59으로 최종 정산
    for car, is_parking in parking_info.items():
        if is_parking:
            time_info[car] += 23*60 + 59

    # 요금 정산
    for car in sorted(time_info): # time_info의 key 기준으로 정렬됨
    #for car, time in time_info.items():
        fee = get_fee(time)
        answer.append(fee)

    return answer

# [14600, 34400, 5000]
print(solution(
    [180, 5000, 10, 600],
    ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"],
))

# [0, 591]
print(solution(
    [120, 0, 60, 591],
    ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]
))

# [14841]
print(solution(
    [1, 461, 1, 10],
    ["00:00 1234 IN"]
))
