# [PCCE 기출문제] 10번, 데이터 분석
## 문제) 기준에 따른 데이터 정렬

def solution(data, ext, val_ext, sort_by):
    
    chk_data = []
    
    if ext == "code":
        print(0)
        ext_i = 0
    elif ext == "date":
        print(1)
        ext_i = 1
    elif ext == "maximum":
        ext_i = 2
    elif ext == "remain":
        ext_i = 3
        
    if sort_by == "code":
        sort_by_i = 0
    elif sort_by == "date":
        sort_by_i = 1
    elif sort_by == "maximum":
        sort_by_i = 2
    elif sort_by == "remain":
        sort_by_i = 3
        
    for i in range(0, len(data)):
        if data[i][ext_i] < val_ext:
            chk_data.append(data[i])
    
    chk_data.sort(key=lambda x: x[sort_by_i])
    return chk_data      

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))


# 풀이
## date를 data로 쓰는 오타가 있었다
## 조건문이 너무 많아서 줄일 필요가 있다. 딕셔너리나 ext의 인덱스 값(list.index 사용)을 비교하는게 방법이 될 수 있다