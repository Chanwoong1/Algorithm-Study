def solution(k, score):
    answer = []
    q = []
    for s in score :
        q.append(s)
        q.sort(reverse = True)
        if (len(q) < k) :
            answer.append(q[-1])
        else :
            answer.append(q[k - 1])
    return answer