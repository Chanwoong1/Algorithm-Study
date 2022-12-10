import math
def solution(a, b):
    answer = b // math.gcd(a, b)
    set_lst = set()
    d = 2
    while d <= answer:
        if answer % d == 0:
            set_lst.add(d)
            answer /= d
        else:
            d += 1
    set_lst.discard(2)
    set_lst.discard(5)
    if len(set_lst) == 0 :
        return 1
    return 2