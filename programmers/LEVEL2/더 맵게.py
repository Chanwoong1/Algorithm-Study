'''
https://programmers.co.kr/learn/courses/30/lessons/42626
'''

import heapq    # 힙 자료구조 사용
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 기존 리스트를 힙 구조로 변환
    while scoville[0] < K :
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)   # 가장 낮은 두 값을 빼주면서 동시에 연산에 활용
        heapq.heappush(scoville, mix)   # 연산된 mix를 다시 scoville에 포함시킴
        answer += 1                     # 이를 반복하면 scoville의 수는 점점 줄어들게 된다.
        if len(scoville) == 1 and scoville[0] < K : # 예외조건
            return -1
    return answer