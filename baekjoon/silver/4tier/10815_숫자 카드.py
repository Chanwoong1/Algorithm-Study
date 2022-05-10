# https://www.acmicpc.net/problem/10815

n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))
answer = []
n_lst.sort()

# 이진탐색 - 검색 범위를 줄여나가며 데이터를 검색하는 알고리즘
def binary_search(arr, target, start, end) :
    while (start <= end) :
        mid = (start + end) // 2

        if arr[mid] == target :
            return 1
        elif arr[mid] > target :
            end = mid - 1
        else :
            start = mid + 1
    return 0

for i in range(m) :
    if binary_search(n_lst, m_lst[i], 0, n - 1) == 1 :
        answer.append("1")
    else :
        answer.append("0")
print(' '.join(answer))