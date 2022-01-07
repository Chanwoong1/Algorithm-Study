# https://www.acmicpc.net/problem/15873

a = input()
if '10' in a :
    a = a.replace('10', ' 10 ')
    a = a.split()
    print(sum([int(i) for i in a]))
else :
    a = list(a)
    print(sum([int(i) for i in a]))