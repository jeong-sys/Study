def solution(id_list, report, k):

    answer = []
    # report값 : 신고 한 사람, 신고 받은 사람 동일할 때 삭제해주기
    report_f = set(report)
    print('1',report_f)

    # id_list값 모두 0으로 설정(딕셔너리) => 리스트 딕셔너리 변환
    id_dic = {id:0 for id in id_list}
    print('2',id_dic)

    # report에 배열[1] 값만 불러와서 횟수 세기(딕셔너리 사용해보기)
    ## 리스트 사용해서 분류하여 딕셔너리에 저장하기
    called_list = []

    for called_id in report_f:
        called_list.append((called_id.split())[1])
    print('3',called_list)

    #초기화된 딕셔너리에 위의 리스트 값 키 겹치면 저장
    for called_id2 in called_list:
        if(id_dic[called_id2] != None):
            id_dic[called_id2] += 1
        else:
            pass
    print('4',id_dic)

    # 신고 받은 횟수가 k번 이상일 때, 신고 한 사람한테 메일 보내기
    ## k번 이상 신고 받은 사람 찾기
    ## *** dictionary로 찾으려고 했는데 안돼서 list로 분류해서 찾음    

    user = list(id_dic.keys())
    num = list(id_dic.values())

    print('0', user, num)
    idx_list = []
    idx_f = 0

    ## idx로 사람 정보 append
    ## 신고 받은 사람 : 리스트로 만들기
    for n in num:
        if n >= k:
            idx_list.append(user[idx_f])
        idx_f += 1
    print('00', idx_list)

    ## 신고 받은 사람(idx_list)을 통해서 처음 리스트(report_f)로 신고 한 사람 찾기
    # 처음 리스트 : 분류해서 리스트로 만들기
    report_list = list(report_f)
    report_list2 = []
    for r in report_list:
        report_list2.append(r.split())
    
    print('000',report_list2)

    # 신고 받은 사람의 리스트가 처음 리스트에 있을때 처음 리스트 내의 신고 한 사람 뽑기
    idx_f2 = 0
    final_call_user = []
    for find in report_list2:
        for find2 in idx_list:
            if find2 == find[1]:
                final_call_user.append(report_list2[idx_f2])
        idx_f2 += 1
    
    print(final_call_user)  

    #유저가 받은 메일 수
    ## 원래 주는 아이디랑 비교해서 딕셔너리 0에서 final_call_user[0] 있으면 하나씩 증가

    print('h', id_list)
    main_dic = {id:0 for id in id_list}
    for mail in final_call_user:
        mail = mail[0]
        if(main_dic[mail] != None):
            main_dic[mail] += 1
        else:
            pass
    print('a', main_dic)

    answer = list(main_dic.values())
    
    return answer
     
# [2, 1, 1, 0]
print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi", "apeach muzi"], 2))
# [0, 0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))

'''
python - pycharm
c - vscode
java - eclipse
'''