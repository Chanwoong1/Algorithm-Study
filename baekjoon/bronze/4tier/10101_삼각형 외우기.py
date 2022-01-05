# https://www.acmicpc.net/problem/10101

A = int(input())
B = int(input())
C = int(input())
if A + B + C == 180 :
    if A == B and A == C :
        print('Equilateral')
    elif A == B :
        print('Isosceles')
    elif B == C : 
        print('Isosceles')
    elif A == C :
        print('Isosceles')
    else :
        print('Scalene')
else :
    print('Error')