def solution(queue1, queue2):
    tmp = (sum(queue1) + sum(queue2)) // 2
    if (max(queue1 + queue2) > tmp) : return -1
    answer1 = 0
    start = 0
    end = len(queue1) - 1
    lst1 = queue1 + queue2 + queue1
    tmp1 = sum(queue1)
    while tmp1 != tmp :
        if tmp1 < tmp :
            end += 1
            if end == len(lst1) : return -1
            tmp1 += lst1[end]
        else :
            tmp1 -= lst1[start]
            start += 1
        answer1 += 1
    answer2 = 0
    start = 0
    end = len(queue2) - 1
    lst2 = queue2 + queue1 + queue2
    tmp2 = sum(queue2)
    while tmp2 != tmp :
        if tmp2 < tmp :
            end += 1
            tmp2 += lst2[end]
        else :
            tmp2 -= lst2[start]
            start += 1
        answer2 += 1
    return min(answer1, answer2)