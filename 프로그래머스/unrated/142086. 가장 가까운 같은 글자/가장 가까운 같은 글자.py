def solution(s):
    answer = []
    for i in range(len(s)) :
        tmp = True
        for j in range(i - 1, -1, -1) :
            if s[i] == s[j] :
                answer.append(i - j)
                tmp = False
                break
        if tmp :
            answer.append(-1)
    return answer