# 행렬 테두리 회전하기
## rows x columns 크기의 행렬이 존재할 때, (x1, y1, x2, y2) 입력이 들어온다
## x1, y1 에서 시계방향으로 x2,y2 까지 회전할때 가장 작은 수 출력하기
## 이때 배열 크기에 따라 1~ nxn 까지 숫자 부여함

def solution(rows, columns, queries):

    # 1. 1씩 증가하는 행렬을 생성한다.
    ## 1 ~ rows x columns 리스트 --> x , 2차원 행렬로 해야함
    matrix = [[(i) * columns + (j + 1) for j in range(columns)] for i in range(rows)]

    # 2. 회전해야 할 위치들의 값을 받아온다.
    result = []
    for x1, y1, x2, y2 in queries:
        result.append(rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1, matrix))

    return result

# 3. 행렬을 시계 방향으로 회전시킨다.
# 4. 3번의 과정에서 최솟값을 찾는다 (변수에 담는다)
def rotate(x1, y1, x2, y2, matrix):
    first = matrix[x1][y1]
    min_value = first

    # 왼쪽
    for k in range(x1, x2):
        matrix[k][y1] = matrix[k+1][y1]
        min_value = min(min_value, matrix[k+1][y1])
    
    #아래
    for k in range(y1, y2):
        matrix[x2][k] = matrix[x2][k+1]
        min_value = min(min_value, matrix[x2][k+1])

    #오른쪽
    for k in range(x2, x1, -1):
        matrix[k][y2] = matrix[k-1][y2]
        min_value = min(min_value, matrix[k-1][y2])

    # 위
    for k in range(y2, y1 + 1, -1):
        matrix[x1][k] = matrix[x1][k-1]
        min_value = min(min_value, matrix[x1][k-1])

    matrix[x1][y1 + 1] = first
    return min_value

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])) # result : [8, 10, 25]