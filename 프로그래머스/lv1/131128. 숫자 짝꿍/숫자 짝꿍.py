def solution(X, Y):
    answer = ''
    x_lst = [0] * 10
    y_lst = [0] * 10
    for i in range(len(X)) :
        x_lst[int(X[i])] += 1
    for i in range(len(Y)) :
        y_lst[int(Y[i])] += 1
    for i in range(9, -1, -1) :
        for j in range(min(x_lst[i], y_lst[i])) :
            answer += str(i)
    if len(answer) == 0 :
        answer = "-1"
    elif answer[0] == '0':
        answer = "0"
    return answer