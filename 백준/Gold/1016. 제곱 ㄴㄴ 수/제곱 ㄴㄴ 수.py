import math

_min, _max = map(int, input().split())
answer = [1 for _ in range(_max - _min + 1)]
i = 2
while i ** 2 <= _max :
    tmp = _min // i ** 2
    while tmp * (i ** 2) <= _max :
        if (tmp * (i ** 2) >= _min) :
            answer[tmp * (i ** 2) - _min] = 0
        tmp += 1
    i += 1
print(sum(answer))