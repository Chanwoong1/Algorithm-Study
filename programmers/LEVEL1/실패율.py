'''
https://programmers.co.kr/learn/courses/30/lessons/42889
'''

def solution(N, stages):
    rate_dict = {}
    for n in range(1, N + 1) :
        stop_players = len([i for i in stages if i == n])   # 멈춰있는 사용자의 수
        clear_players = len([i for i in stages if i > n])   # 스테이지에 도달한 플레이어 수
        if stop_players == 0 and clear_players == 0 :       # 둘 다 0인 경우
            rate_dict[n] = 0
        elif clear_players == 0 :                           # 도달한 유저가 0인 경우
            clear_players = 1e-3                            # 계산 불가 방지
            rate_dict[n] = stop_players/clear_players
        else :
            rate_dict[n] = stop_players/clear_players
    rate_dict = [i[0] for i in sorted(rate_dict.items(), key=lambda x : x[1], reverse = True)]  # value 기준 내림차순으로 정렬
    answer = rate_dict
    return answer