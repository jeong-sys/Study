# PCCP 기출문제 1번, 붕대감기
## t초 붕대 : 1초 동안 x 체력 회복 가능 // t*x

## 전체조건 : 시간은 1초 기준으로 흐르고 있음
## 몬스터 마지막 공격 파악 : 0~마지막 공격 시간 파악, attacks마지막 배열[0]
## 최대 체력 이상 가질 수 없음 : (y가 가능한 숫자는 누적 = t_y ++1), t == t_y인경우 +y ,, t_y = 0
## 해당시간 공격 -> 몬스터로 인한 체력 감소(health - 피해량), 공격 당할 시 t_y = 0
## 마지막 공격까지 살면 남은 체력 return, 죽으면 -1 return

def solution(bandage, health, attacks):
    ## bandage[시전시간(t), 초당회복량(x), 추가회복량(y)]
    ## health : 최대체력
    ## attacks[[공격시간1, 피해량2],[공격시간2, 피해량2]...]
    
    attacks_len = len(attacks)-1
    attacks_final = attacks[attacks_len][0]
    
    leave_time = 0
    player_health = health
    y_time = 0
    attack_i = 0
    
    # 마지막 공격 시간까지 계속함, leave_time은 살아있는 시간으로 1초씩 증가
    while attacks_final+1 != leave_time:
        
        print("현재 시간", leave_time)
            
        # 공격 파악 --> 반복(?) 돌려야함 // 반복 없이 확인
        if leave_time == attacks[attack_i][0]:
            print("공격 시간", leave_time, attacks[attack_i][0])
            print("attack전 체력", player_health)
            player_health = player_health - attacks[attack_i][1]
            print("attack후 체력", player_health)
            
            if player_health <= 0:
                return -1
    
            y_time = 0 # 공격받았으니 초기화
            
            # 하나씩 증가 -> 증가가 안되네 -> attack_i+=1이라서 안됨
            attack_i = attack_i + 1
            
        # 1초에 x증가, y_time 누적
        else:
            if y_time != bandage[0]:
                print("y 체력 여부 확인", y_time, bandage[0])
                if player_health < health:
                    # 더한값이 health를 넘어가면 안됨
                    player_health_ch = player_health + bandage[1] # 1초에 x추가
                    
                    # 최댓 값 넘어가면, 최댓값으로 설정
                    if player_health_ch > health:
                        player_health = health                     
                    else:
                        player_health = player_health_ch
                    
                    y_time += 1
                print("누적 y 확인", y_time)  
                print("현재 체력", player_health)

            # 누적 시간 확인(y체력 줄 수 있는가), 1초.1초인 경우 바로 실행되야 하므로 elif말고 if
            if y_time == bandage[0]:
                if player_health < health:
                    print("y 체력 여부 확인",y_time, bandage[0])
                    print("y 체력 전 확인", player_health)
                    
                    player_health_ch = player_health + bandage[2]
                    
                    if player_health_ch > health:
                        player_health = health
                    else:
                        player_health = player_health_ch
                              
                    print("y 체력 후 확인", player_health)  ## 문제
                    y_time = 0 # 체력 부여 했으니 y_time 초기화

            # 아닌경우 일반적인 체력 부여 --> 순서가 체력 부여 먼저 ,, 그리고 추가 체력 부여로 바뀌어야함
            # else:
                
        leave_time += 1
        
    return player_health


# print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))  # result 5
# print(solution([1, 1, 1], 5, [[1, 2], [3, 2]])) # result 3
print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])) # result -1