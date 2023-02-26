def solution(keymap, targets):
    answer = []
    key = [-1] * 26;
    alpha = "ABCDEFGHIJKMLNOPQRSTUVWXYZ"
    for i in range(len(alpha)) :
        for k in keymap :
            if k.find(alpha[i]) != -1 :
                if key[i] == -1 :
                    key[i] = k.find(alpha[i]) + 1
                else :
                    key[i] = min(key[i], k.find(alpha[i]) + 1)
    for target in targets :
        idx = 0
        for t in target :
            if (key[alpha.find(t)] == -1) :
                idx = -1
                break
            else :
                idx += key[alpha.find(t)]
        answer.append(idx)
    return answer