# https://www.acmicpc.net/problem/6763

N = int(input())
F = int(input())
tmp = N - F
if tmp <= -31 :
    print('You are speeding and your fine is $500.')
elif tmp <= -21 :
    print('You are speeding and your fine is $270.')
elif tmp <= -1 :
    print('You are speeding and your fine is $100.')
else :
    print('Congratulations, you are within the speed limit!')