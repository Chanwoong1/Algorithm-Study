# https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3

# 정확성 통과, 효율성 실패(시간초과)
def solution(info, query):
    answer = []
    info_list = [i.split() for i in info]
    query_list = [' '.join(' '.join(i.split(' and ')).split('-')).split() for i in query]
    for i in query_list :
        i_score = int(i.pop())
        q = 0
        for j in info_list :
            _j = ''.join(j)
            tmp = [q for q in i if q not in _j]
            if len(tmp) == 0 and i_score <= int(j[-1]) :
                q += 1
        answer.append(q)
    return answer

# 효율성 개선
from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for i in info:
        temp = i.split(" ")
        key = temp[0:-1]
        score = int(temp[-1])

        for j in range(5):
            combi = list(combinations(key, j))
            for c in combi:
                temp_key = ''.join(c)
                info_dict[temp_key].append(score)

    for key in info_dict.keys():
        info_dict[key].sort()

    for q in query:
        q = q.split(" ")
        query_score = int(q[-1])
        query_key = q[:-1]

        for _ in range(3):
            query_key.remove("and")

        while "-" in query_key:
            query_key.remove("-")
        query_key = ''.join(query_key)

        if query_key in info_dict:
            scoreList = info_dict[query_key]

            if len(scoreList) > 0:
                left, right = 0, len(scoreList)
                while left < right:
                    mid = (left + right) // 2
                    if scoreList[mid] >= query_score:
                        right = mid
                    else:
                        left = mid + 1
                answer.append(len(scoreList) - left)
        else:
            answer.append(0)

    return answer