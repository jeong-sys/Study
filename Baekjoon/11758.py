# 1175번 CCW 문제
## 단순하게 y좌표만으로 구하고, 기울기를 통해서 구하는 것에서는 한계가 있음
## 기하 알고리즘으로 구할 수 있는 방법이 있음
## CCW에 대해 먼저 알아야함

p = []
for _ in range(3):
    p.append(list(map(int, input().split())))

def ccw(p_1, p_2, p_3):
    val = (p_1[0]*p_2[1] + p_2[0]*p_3[1] + p_3[0]*p_1[1]) - (p_2[0]*p_1[1] + p_3[0]*p_2[1] + p_1[0]*p_3[1])
    return val

result = ccw(p[0], p[1], p[2])

if result > 0:
    print(1)
elif result == 0:
    print(0)
else:
    print(-1)