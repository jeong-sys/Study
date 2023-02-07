def solution(id_list, report, k):

    answer = [] # 정답
    '''1회 신고 적용'''
    report_f = set(report) # report중복 제거
    
    id_dic = {id:0 for id in id_list} # id_list 딕셔너리 저장(0으로 초기화)
    #신고 받은 사람
    called_list = [] # 신고 받은 사람
    called_list_k = [] # k번 이상 신고 받은 사람
    #신고 한 사람
    call_list = [] # [신고 한 사람, 신고 받은 사람] 
    call_list_k = [] # k번 이상 [신고 한 사람, 신고 받은 사람]
    
    '''신고 받은 횟수 비교'''
    for called_id in report_f: # 신고 받은 사람만 리스트 생성
        called_list.append((called_id.split())[1]) 

    for called_id2 in called_list: # 신고 받은 사람 횟수 추가 // 딕셔너리로 표현
        if(id_dic[called_id2] != None):
            id_dic[called_id2] += 1
        else:
            pass

    '''k번 이상 신고 받은 사람 => 다시 리스트로 변환'''
    called_id_k = list(id_dic.keys())
    called_k = list(id_dic.values())

    idx_f = 0 # k번 이상 신고 받은 사람 index
    for num in called_k:
        if num >= k:
            called_list_k.append(called_id_k[idx_f])
        idx_f += 1

    '''신고 받은 사람(1차원 배열) 기준으로 신고 한 사람(2차원 배열[0]) 찾기'''
    '''신고 한 사람 찾기 // 리스트 변환'''
    report_list = list(report_f)
    for r in report_list:
        call_list.append(r.split())

    '''k번 이상 신고받은 사람을 신고한 사람 // 리스트 변환'''
    idx_f2 = 0
    for call in call_list:
        for call2 in called_list_k:
            if call2 == call[1]:
                call_list_k.append(call_list[idx_f2])
        idx_f2 += 1
    
    '''k번 이상 신고 받은 사람만 리스트 생성 = call_list_k
        신고 한 사람이 받는 메일 수'''
    mail_dic = {id:0 for id in id_list} # id_list 딕셔너리로 0초기화
    print(call_list_k)
    for mail in call_list_k: # 신고 한 사람 겹치면 1추가
        mail = mail[0]
        if(mail_dic[mail] != None):
            mail_dic[mail] += 1
        else:
            pass
    
    '''답 출력'''
    answer = list(mail_dic.values())
    return answer
     
print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi", "apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
