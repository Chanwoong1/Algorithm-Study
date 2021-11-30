'''
https://programmers.co.kr/learn/courses/30/lessons/12982
'''

def solution(d, budget):
    d = sorted(d)           # 신청 예산이 낮은 부서부터 지
    n = 0
    if sum(d) == budget :   # 예산과 신청한 금액의 합이 같다면
        return len(d)       # 모든 부서의 수 출력
    else :
        for i in d :
            if budget < i : # 예산이 부서의 신청 금액보다 낮아질 경우
                return n    # 중지
            budget -= i
            n += 1
        return n            # 예산이 남을 경우 출력