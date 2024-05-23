# 위클리 챌린지, 부족한 금액 계산하기
## 놀이공원 이용료 계산(ex. 처음 이용료 100, 두번째 200, 세번쨰 300 / count번에 따라 자신의 금액이 얼마나 모자라는지 return)

def solution(price, money, count):
    
    need_money = 0
    i = 1
    for i in range(count+1): 
        print(count)
        need_money += i * price # 3 + 6 + 9 + 12 
    
    if money < need_money:
        answer = need_money - money
    elif money >= need_money:
        answer = 0

    return answer


# result = 10
print(solution(3, 20, 4)) # 3 + 6 + 9 + 12 = 30

## 풀이 : 직관적이며 어렵지 않았다