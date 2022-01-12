# https://www.acmicpc.net/problem/19602

h = int(input())
h += int(input()) * 2
h += int(input()) * 3
if h >= 10 :
    print('happy')
else :
    print('sad')