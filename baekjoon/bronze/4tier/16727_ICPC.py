# https://www.acmicpc.net/problem/16727

p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())
p = p1 + p2
s = s1 + s2
if p == s :
    if s1 < p2 :
        print('Persepolis')
    elif s1 > p2 :
        print('Esteghlal')
    else :
        print('Penalty')
elif p < s :
    print('Esteghlal')
else :
    print('Persepolis')