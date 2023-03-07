def solution(n, words):
    overlap = set()
    overlap.add(words[0])
    answer = []
    idx = 1
    order = 2
    tmp = 1
    while idx < len(words) :
        if words[idx] in overlap :
            break
        if words[idx - 1][-1] != words[idx][0] : 
            break
        overlap.add(words[idx])
        idx += 1
        order += 1
        if order > n :
            order = 1
            tmp += 1
    if idx == len(words) : answer = [0, 0]
    else : answer = [order, tmp]
    return answer