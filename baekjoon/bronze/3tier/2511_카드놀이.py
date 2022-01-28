# https://www.acmicpc.net/problem/2511

a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))
last_winner = 'D'
a_score = 0
b_score = 0
for i in range(len(a_lst)) :
    if a_lst[i] > b_lst[i] :
        a_score += 3
        last_winner = 'A'
    elif a_lst[i] == b_lst[i] :
        a_score += 1
        b_score += 1
    else :
        b_score += 3
        last_winner = 'B'
print(a_score, b_score)
if a_score > b_score :
    print('A')
elif a_score == b_score :
    if last_winner == 'A' :
        print('A')
    elif last_winner == 'B' :
        print('B')
    else :
        print('D')
else :
    print('B')