# https://www.acmicpc.net/problem/2110

import sys
input = sys.stdin.readline
N, C = map(int, input().split())
lst = sorted([int(input()) for _ in range(N)])

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1

        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= C:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

start = 1
end = lst[-1] - lst[0]
answer = 0
binary_search(lst, start, end)
print(answer)