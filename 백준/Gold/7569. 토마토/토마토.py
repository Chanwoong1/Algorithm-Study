M, N, H = map(int, input().split())
box = []
for _ in range(N * H) :
    box += list(map(int, input().split()))	# 1차원으로 받아줬다

day = 0
move = [1, -1, M, -M, M * N, -M * N]	# 1차원 상하좌우
to_lst = [set([i for i in range(len(box)) if box[i] == 1])]	# 0일째 토마토 위치
while 1 :
    cnt = 0
    day_tomato = to_lst.pop(0)
    next = set()
    for idx in list(day_tomato) :
        if idx + 1 < M * N * H and (idx + 1) % M != 0 and box[idx + 1] == 0:	# 조건에 만족하면 옆칸에 토마토 심을 수 있음
            box[idx + 1] = 1
            next.add(idx + 1)
            cnt += 1
        if idx - 1 >= 0 and idx % M != 0 and box[idx - 1] == 0 :
            box[idx - 1] = 1
            next.add(idx - 1)
            cnt += 1
        if idx + M < M * N * H and idx % (M * N) - (M * (N - 1)) < 0 and box[idx + M] == 0 :
            box[idx + M] = 1
            next.add(idx + M)
            cnt += 1
        if idx - M >= 0 and idx % (M * N) >= M and box[idx - M] == 0 :
            box[idx - M] = 1
            next.add(idx - M)
            cnt += 1
        if idx + M * N < M * N * H and box[idx + M * N] == 0 :
            box[idx + M * N] = 1
            next.add(idx + M * N)
            cnt += 1
        if idx - M * N >= 0 and box[idx - M * N] == 0 :
            box[idx - M * N] = 1
            next.add(idx - M * N)
            cnt += 1
    if cnt == 0 :	# 하나도 못심었다면 다 심은거임
        break
    day += 1
    if len(next) > 0 :
        to_lst.append(next)
    
    
    # print()
    # for i in range(N * H) :
    #     print(*box[M * i : M * (i + 1)])
        
if len([1 for i in box if i == 0]) > 0 :
	print(-1)
else :
	print(day)