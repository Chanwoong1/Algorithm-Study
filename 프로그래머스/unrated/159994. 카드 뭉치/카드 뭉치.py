def solution(cards1, cards2, goal):
    i = 0
    j = 0
    while i + j < len(goal) :
        if i < len(cards1) and cards1[i] == goal[i + j] :
            i += 1
        elif j < len(cards2) and cards2[j] == goal[i + j] :
            j += 1
        else :
            return "No"
    return "Yes"