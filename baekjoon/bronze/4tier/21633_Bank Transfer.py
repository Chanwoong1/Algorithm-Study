# https://www.acmicpc.net/problem/21633

k = int(input()) * 0.01 + 25
if k < 100 :
    print(f'{100 :.2f}')
elif k > 2000 :
    print(f'{2000 :.2f}')
else :
    print(f'{k :.2f}')