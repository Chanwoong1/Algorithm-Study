def solution(today, terms, privacies):
    today = list(map(int, today.split('.')))
    split_terms = [i.split() for i in terms]
    answer = []
    for i in range(len(privacies)) :
        tmp, priv = privacies[i].split()
        j = 0
        while j < len(split_terms) :
            if split_terms[j][0] == priv : break
            j += 1
        period = list(map(int, tmp.split('.')))
        period[1] += int(split_terms[j][1])
        period[2] -= 1
        if period[2] == 0 :
            period[2] = 28
            period[1] -= 1
        if period[1] > 12 :
            period[1] -= 12
            period[0] += 1
        elif period[1] == 0 :
            period[1] = 12
            period[0] -= 1
        p = (period[0] * 12 + period[1]) * 28 + period[2]
        s = (today[0] * 12 + today[1]) * 28 + today[2]
        # print(period, priv, i + 1, p, s)
        if p < s : answer.append(i + 1)
    return answer