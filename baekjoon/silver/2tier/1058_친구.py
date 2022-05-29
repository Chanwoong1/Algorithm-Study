# https://www.acmicpc.net/problem/1058

N = int(input())
friends = []
for _ in range(N) :
    friends.append(list(input()))
visit = [[0] * N for _ in range(N)]
for x in range(N) :
    for y in range(N) :
        for z in range(N) :
            if y == z :
                continue
            if friends[y][z] == 'Y' or (friends[y][x] == 'Y' and friends[x][z] == 'Y') :
                visit[y][z] = 1
answer = 0
for i in range(N) :
    tmp = 0
    for j in range(N) :
        if visit[i][j] == 1 :
            tmp += 1
    answer = max(answer, tmp)
print(answer)