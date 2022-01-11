# https://www.acmicpc.net/problem/17009

apple = int(input()) * 3
apple += int(input()) * 2
apple += int(input())
banana = int(input()) * 3
banana += int(input()) * 2
banana += int(input())
if apple == banana :
    print('T')
elif apple < banana :
    print('B')
else :
    print('A')