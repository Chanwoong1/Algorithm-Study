def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    for bb_idx in range(len(babbling)) :
        prev = ""
        w_idx = 0
        while w_idx < 4 :
            if prev != word[w_idx] and babbling[bb_idx][0 : len(word[w_idx])] == word[w_idx] :
                babbling[bb_idx] = babbling[bb_idx][len(word[w_idx]) :]
                prev = word[w_idx]
                w_idx = -1
            w_idx += 1
        if len(babbling[bb_idx]) == 0 :
            answer += 1
    return answer
