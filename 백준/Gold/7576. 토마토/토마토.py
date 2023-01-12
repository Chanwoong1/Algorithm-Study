M, N = map(int, input().split())
box = []
for _ in range(N) :
    box += list(map(int, input().split()))

day = 0
move = [1, -1, M, -M]
tomato_location = [[i for i in range(len(box)) if box[i] == 1]]
while 1 :
    cnt = 0
    day_tomato = tomato_location.pop(0)
    next = []
    for tomato_idx in day_tomato :
        if tomato_idx + 1 < M * N and (tomato_idx + 1) % M != 0 and box[tomato_idx + 1] == 0:
            box[tomato_idx + 1] = 1
            next.append(tomato_idx + 1)
            cnt += 1
        if tomato_idx - 1 >= 0 and tomato_idx % M != 0 and box[tomato_idx - 1] == 0 :
            box[tomato_idx - 1] = 1
            next.append(tomato_idx - 1)
            cnt += 1
        if tomato_idx + M < M * N and box[tomato_idx + M] == 0 :
            box[tomato_idx + M] = 1
            next.append(tomato_idx + M)
            cnt += 1
        if tomato_idx - M >= 0 and box[tomato_idx - M] == 0 :
            box[tomato_idx - M] = 1
            next.append(tomato_idx - M)
            cnt += 1
    if cnt == 0 :
        break
    day += 1
    if len(next) > 0 :
        tomato_location.append(next)
        
if len([1 for i in box if i == 0]) > 0 :
	print(-1)
else :
	print(day)