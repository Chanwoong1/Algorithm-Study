# https://www.acmicpc.net/problem/18005

n = int(input())
even = n // 2
odd = n // 2
if n != even + odd :
    print(0)
else :
    if even % 2 == 0 :
        print(2)
    else :
        print(1)