def solution(msg):
    s = list("0ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    idx = 0
    tmp = ""
    answer = []
    while idx < len(msg):
        end = 1
        while idx + end <= len(msg):
            tmp = msg[idx:idx+end]
            if tmp in s:
                end += 1
            else:
                s.append(tmp)
                answer.append(s.index(tmp[:-1]))
                idx += end - 1
                break
        else:  # while-else 구문 활용
            answer.append(s.index(tmp))
            idx += end
    return answer
