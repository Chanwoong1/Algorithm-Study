n = int(input())
lst = [*map(int, input().split())]
x = int(input())
lst.sort()
ans, start, end = 0, 0, len(lst) - 1
while start < end:
    if lst[start] + lst[end] < x:
        start += 1
    elif lst[start] + lst[end] > x:
        end -= 1
    else:
        ans += 1
        start += 1
print(ans)
