# https://www.acmicpc.net/problem/1931

N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
lst = sorted(lst, key = lambda x : (x[1], x[0]))    # 끝나는 시간부터 정렬, 끝나는 시간이 동일하다면 시작시간으로 정렬

start = lst[0][0]   # 맨 처음 값 미리 입력
end = lst[0][1]
n = 1
for i in range(1, len(lst)) :
    if lst[i][0] >= end :
        start = lst[i][0]
        end = lst[i][1]
        n += 1
print(n)
