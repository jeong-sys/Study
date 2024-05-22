# [PCCE 기출문제] 9번, 이웃한 칸
## 문제) 2차 격자 보드판에서 h,w를 기준으로 왼쪽, 오른쪽, 위, 아래가 같은 색깔인 경우의 숫자를 찾아라

def solution(board, h, w):
    
    n = len(board)
    answer = 0
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    if 0 <= n <= 7:
        for i in range(0, 4):
            h_check = h + dh[i]
            w_check = w + dw[i]
            print(h_check, w_check)
            
            if 0 <= h_check < n and 0<= w_check < n:
                if board[h][w] == board[h_check][w_check]:
                    answer += 1
    
    return answer


print(solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], 
                ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]],1,1))

# 에러
## 런타임 에러
## - 18번째 줄을 if 0 <= h_check & w_check < n: 지정했는데 여기서 런타임 오류가 발생했다
## - and는 논리 연산자이고 &는 비트 연산자로 True 반환이 아닌 0,1 반환으로 오류가 발생했다