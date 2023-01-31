def solution(id_list, report, k):

    # report값 : 신고 한 사람, 신고 받은 사람 동일할 때 삭제해주기
    report_f = set(report)
    print(report_f)

    # id_list값 모두 0으로 설정(딕셔너리) => 리스트 딕셔너리 변환
    id_dic = {id:0 for id in id_list}
    #print(id_dic)

    # report에 배열[1] 값만 불러와서 횟수 세기(딕셔너리 사용해보기)
    ## 리스트 사용해서 분류하여 딕셔너리에 저장하기
    called_list = []

    for called_id in report_f:
        called_list.append((called_id.split())[1])
    #print(called_list)

    #초기화된 딕셔너리에 위의 리스트 값 키 겹치면 저장
    for called_id2 in called_list:
        if(id_dic[called_id2] != None):
            id_dic[called_id2] += 1
        else:
            pass
    #print(id_dic)

    # 신고 받은 횟수가 k번 이상일 때, 신고 한 사람한테 메일 보내기
    ## k번 이상 신고 받은 사람 찾기

    num_list = []
    for num in id_dic.values():
        if num >= k:
            num_list.append(id_dic.keys())

    print(num_list)

    ## 신고 받은 사람을 통해서 처음 리스트로 신고 한 사람 찾기
    # 신고 받은 사람 : 리스트로 만들기
    # 처음 리스트 : 분류해서 리스트로 만들기
    # 신고 받은 사람의 리스트가 처음 리스트에 있을때 처음 리스트 내의 신고 한 사람 뽑기

    answer = []

# [2, 1, 1, 0]
print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi", "apeach muzi"], 2))
# [0, 0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))


# num_police = {
#     "muzi":0,
#     "frodo":2,gi
#     "apeach":0,
#     "neo":2,
# }
#
# num_mail = {
#     "muzi": 2,
#     "frodo": 1,
#     "apeach": 1,
#     "neo": 0,
# }

# ###############==============
# # 신고 내역
# history = {}
# # 신고 횟수 저장
# report_count = {}
# # 초기화
# for x in report:
#     print(x)

### 디버깅 ~
'''
python - pycharm
c - vscode
java - eclipse
'''