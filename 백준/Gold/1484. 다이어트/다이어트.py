G = int(input())
lst = [int(x**2) for x in range(100001)]

prev, curr = 1, 2
answer = []
while True:
    if curr - prev == 1 and lst[curr] - lst[prev] > 100000:
        break

    if lst[curr] - lst[prev] < G:
        curr += 1
    elif lst[curr] - lst[prev] > G:
        prev += 1
    else:
        answer.append(curr)
        prev += 1

if answer:
    [print(x) for x in answer]
else:
    print(-1)
