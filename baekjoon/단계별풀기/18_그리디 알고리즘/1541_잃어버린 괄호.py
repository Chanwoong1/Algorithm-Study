# https://www.acmicpc.net/problem/1541

# 풀이방법 : -가 나올때마다 구분지어서 남은 '+'들은 모두 괄호쳐서 먼저 합해준뒤
# 맨 처음 값을 제외한 나머지 값들을 전부 빼준다
sol = list(input().split('-'))  # '-'나올때 구분해주기

# 리스트 값에 있는 '+'들을 풀어준다.
gr = []
for i in sol :
    if '+' in i :
        gr.append(list(map(int, i.split('+'))))
    else :
        gr.append([int(i)])

answer = sum(gr[0])     # 초기값
for i in range(1, len(sol)) :
    answer -= sum(gr[i])
print(answer)