def solution(numlist, n):
    answer = []
    for i in range(len(numlist)) :
        tmp = [abs(n - i) for i in numlist]
        value = numlist[tmp.index(min(tmp))]
        values = [i for i in range(len(numlist)) if abs(numlist[i] - n) == min(tmp)]
        if len(values) == 1 :
            answer.append(value)
            numlist.remove(value)
        else :
            answer.append(max(numlist[values[0]], numlist[values[1]]))
            numlist.remove(max(numlist[values[0]], numlist[values[1]]))

    return answer