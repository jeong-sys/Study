'''
재귀를 사용한 DFS로 문제 풀기

    # ex) play(0, 80) => play(1, 80) => play(2, 60) => play(3, 20)
    #                 => play(3, 80) => play(2, 70)
    #                 => play(2, 40)

'''

def solution(k, dungeons):
    # 지금까지 클리어한 던전의 개수
    answer = -1
    # 전체 던전의 수
    dungeons_count = len(dungeons)
    # 던전 번호(idx)로 클리어 여부를 저장
    visited = [False] * dungeons_count

    '''던전을 클리어 했을때 진입 함수'''
    def play(n, current_hp):

        # play 에서 사용하는 answer이 밖에 있는 answer이라는 것을 확인시켜줘야한다.
        # local내 answer이 아님
        nonlocal answer

        '''
        지금까지 클리어한 던전의 수가 최대라면
        '''
        if answer < n:
            # answer 갱신
            answer = n

        '''
        지금까지 깬 던전 수가 던전 개수와 같으면 종료
        깨고나서 남은 hp가 없으면 (==0) 종료
        '''
        if n == dungeons_count or current_hp <= 0:
            # 이 뒤의 코드는 실행하지 않고 이번 play를 종료하겠다.
            return

        '''main code'''
        # 던전 번호 순서대로 순회
        for dungeons_idx in range(dungeons_count):
            # 해당 던전을 방문한 적이 없다면
            if not visited[dungeons_idx]:
                visited[dungeons_idx] = True
                # 요구 피로도, 데미지
                require_hp, damage = dungeons[dungeons_idx]
                # 깰 수 있으면,
                if current_hp >= require_hp:
                    # 깼기 때문에 n+1, 체력은 감소한 채로 다음 던전 탐험
                    play(n+1, current_hp - damage)
                # ** 다음 순회(for)를 위해 시도 하지 않은 걸로 초기화 **
                visited[dungeons_idx] = False

    # tree로 만들기 위해 상위 노드 0으로 둠
    play(0, k)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))