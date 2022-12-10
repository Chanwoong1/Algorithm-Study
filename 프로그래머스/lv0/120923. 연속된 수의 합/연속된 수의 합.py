def solution(num, total):
    tmp = 1000
    while 1 :
        answer = [i for i in range(tmp - num, tmp)]
        if sum(answer) == total :
            break
        tmp -= 1
    return answer