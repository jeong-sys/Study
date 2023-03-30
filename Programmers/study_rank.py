# 순위 검색 문제
## 2021 KAKAO BLIND RECRUITMENT
## [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람?
'''
..? 어려워
info : 지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열
query : 개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열
return : 각 문의조건에 해당하는 사람들의 숫자를 return
'''

def solution(info, query):
    answer = []

    for q in query:
