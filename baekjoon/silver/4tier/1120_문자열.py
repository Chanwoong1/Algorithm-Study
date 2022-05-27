# https://www.acmicpc.net/problem/1120

A, B = list(input().split())
answer = 0
if len(A) == len(B) :
    for _, (i, j) in enumerate(zip(A, B)) :
        if i != j :
            answer += 1
else :
    answer_lst = []
    for i in range(len(B) - len(A) + 1) :
        tmp = 0
        for _, (j, k) in enumerate(zip(A, B[i : i + len(A)])) :
            if j != k :
                tmp += 1
        answer_lst.append(tmp)
    answer = min(answer_lst)
print(answer)