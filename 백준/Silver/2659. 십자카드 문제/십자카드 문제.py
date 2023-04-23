import sys

k = sys.stdin.readline().strip().split()


def sage(k):
    _min = 10000
    for i in range(0, 4):
        _min = min(_min, int("".join(k[i:4] + k[0:i])))
    return _min


_min = sage(k)
index = 0
j = 1111
while j <= _min:
    if "0" not in str(j) and j == sage(list(str(j))):
        index += 1
    j += 1
print(index)
