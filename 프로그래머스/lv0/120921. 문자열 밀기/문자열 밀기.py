from collections import deque
def solution(A, B):
    dq = deque(A)
    i = 0
    while i < len(A) :
        if ''.join(dq) == B :
            break
        dq.rotate(1)
        i += 1
    if i < len(A) :
        return i
    return -1