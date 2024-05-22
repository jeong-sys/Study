def solution(fees, records):
    answer = []
    parking_info = {}
    time_info = {}

    '''주차요금 계산 함수'''
    def get_fee(total_min):
        # 기본 시간, 기본 요금, 단위 시간, 단위 요금 = 요금
        basic_time, basic_fee, unit_time, unit_fee = fees
        # 기본 시간 이상일 경우 추가 요금 계산
        if total_min - basic_time > 0:
            charge_time = total_min - basic_time
            # 올림
            import math
            charge_fee = math.ceil(charge_time / unit_time) * unit_fee

        # 기본 시간 이하일 경우 기본 요금 계산
        else:
            charge_fee = 0

        return basic_fee + charge_fee

    '''시각, 차량 번호, 입출차 내역 = records'''
    for record in records:
        time, car, inout = record.split()

        # 처음 들어온 차량의 경우 데이터 초기화(딕셔너리 사용)
        if not time_info.get(car):
            # 주차시간 0
            time_info[car] = 0
            # 입출차 여부 초기화
            parking_info[car] = False

        # 시간을 분 숫자로 변환
        h, m = map(int, time.split(':'))

        # 입차(-)
        if inout == 'IN':
            time_info[car] -= h * 60 + m
            parking_info[car] = True
        # 출차(+)
        else:
            time_info[car] += h * 60 + m
            parking_info[car] = False

    '''record 순회 이후 주차 중인 차량 시간 정산'''
    for car, is_parking in parking_info.items():
        # 23:59로 최종 정산
        if is_parking:
            time_info[car] += 23*60 + 59

    '''최종 요금 정산'''
    # key 기준으로 정렬
    for car in sorted(time_info):
        fee = get_fee(time_info[car])
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
