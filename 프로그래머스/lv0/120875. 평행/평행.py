from itertools import combinations

def solution(dots):
    answer = []
    for i in combinations(dots, 2) :
        answer.append(abs(i[0][1] - i[1][1]) / abs(i[0][0] - i[1][0]))
    if (len(set(answer)) != 6) :
        return 1;
    return 0;