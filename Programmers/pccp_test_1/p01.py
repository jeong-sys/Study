def solution(input_string):
    answer = ''
    alph_list = []
    alph_list_ov = []

    for i in input_string:
        alph_list.append(i)

    alph_nxt = []

    # 앞뒤 문자가 인덱스 +1 차이인지 확인하기
    for ch in range(len(alph_list) - 1):
        if alph_list[ch] != alph_list[ch+1]:
            alph_nxt += alph_list[ch]
        else:
            pass

    f = len(alph_list) -1
    alph_nxt += alph_list[f]
    alph_dic = {alph: 0 for alph in alph_nxt}

    # 2회 이상인지 확인하기
    # 반복문을 통해서 딕셔너리에 동일한 문자가 존재하면 숫자 증가
    for alph_re in alph_nxt:
        print(alph_re)
        if alph_dic[alph_re] != None:
            alph_dic[alph_re] += 1

    # 2회 이상인 문자만 생성
    for alph_ov in alph_dic:
        if alph_dic[alph_ov] >= 2:
            alph_list_ov.append(alph_ov)

    result = ''.join(s for s in sorted(alph_list_ov))

    if result == "":
        result = "N"

    answer = result

    return answer

print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution("string"))
print(solution("zbzbz"))