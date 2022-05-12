# https://www.acmicpc.net/problem/6588

# import math
# import sys

# input = sys.stdin.readline
# while 1 :
#     N = int(input())
#     if N == 0 :
#         break
#     prime_lst = []
#     arr = [True for i in range(N + 1)]
#     for i in range(2, int(math.sqrt(N)) + 1) :
#         if arr[i] :
#             j = 2
#             while i * j <= N :
#                 arr[i * j] = False
#                 j += 1

#     for num in range(3, N) :
#         if arr[num] :
#             prime_lst.append(num)
    
#     start = 0
#     end = len(prime_lst) - 1
#     while 1 :
#         if prime_lst[start] + prime_lst[end] == N :
#             print(N, "=", prime_lst[start], "+", prime_lst[end])
#             break

#         if prime_lst[start] + prime_lst[end] > N :
#             end -= 1
#         else :
#             start += 1
#         if start > end :
#             print("Goldbach's conjecture is wrong.")
#             break

import sys

def Goldbach():
    check = [False, False] + [True] * 1000000
    
    for i in range(2, 1001):
        if check[i] == True:
            for j in range(i + i, 1000001, i):
                check[j] = False

    while True:
        n = int(sys.stdin.readline())

        if n == 0:
            break

        A = 0
        B = n
        for _ in range(1000000):
            if check[A] and check[B]:
                print(f"{n} = {A} + {B}")
                break
            A += 1
            B -= 1
        else:
            print("Goldbach's conjecture is wrong.")

Goldbach()