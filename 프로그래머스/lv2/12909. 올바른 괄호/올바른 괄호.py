from collections import deque
def solution(s):
    q = deque()
    idx = 0
    while idx < len(s) :
        q.append(s[idx])
        if len(q) >= 2 :
            tmp1 = q.pop()
            tmp2 = q.pop()
            if (tmp2 == '(' and tmp1 == ')') == False :
                q.append(tmp2)
                q.append(tmp1)
        idx += 1
    print(q)
    if (len(q) == 0) :
        return True
    else :
        return False