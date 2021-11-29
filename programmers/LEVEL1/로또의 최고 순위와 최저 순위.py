'''
https://programmers.co.kr/learn/courses/30/lessons/77484
'''

def solution(lottos, win_nums):
    if sorted(lottos) == sorted(win_nums) : # 0이 없고, 모두 다 맞을 경우
        answer = [1, 1]
    else :  # 나머지 경우
        all = 0 # 0이 없으면서 모두 틀릴 경우 찾기위해
        for i in lottos :
            if i != 0 and i not in win_nums :
                all += 1
        if all == 6 :   # 0이 없으면서 모두 틀릴 경우
            answer = [6, 6]
        else :  # 진짜 나머지 경우
            tmp = [0] * 46
            for i in win_nums :
                tmp[i] += 1
            for i in lottos :
                tmp[i] -= 1
            unknown = abs(tmp[0])
            # 못 맞춘 번호 수 (1로 남았을 경우)
            incollect = len([i for i in tmp if i == 1])
            collect = 6 - incollect # 맞춘 번호 수
            # 최고 순위
            max_rank = 7 - (collect + unknown)
            # 최저 순위
            min_rank = 7 - (collect)
            if min_rank == 7 :
                min_rank = 6
            answer = [max_rank, min_rank]
    return answer