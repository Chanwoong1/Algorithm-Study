# https://www.acmicpc.net/problem/1759

L, C = list(map(int, input().split()))
lst = list(input().split())
lst.sort()

answer = []
def solve(step) :
    if step == L :
        aeiou = 0
        etc = 0
        for i in range(step) :
            if answer[i] in 'aeiou' :
                aeiou += 1
            else :
                etc += 1
        if aeiou >= 1 and etc >= 2 :
            print(''.join(answer))

    for i in lst :
        if len(answer) == 0 :
            answer.append(i)
            solve(step + 1)
            aeiou = 0
            etc = 0
            answer.pop()
        
        else :
            if ord(i) > ord(answer[-1]) :
                answer.append(i)
                solve(step + 1)
                answer.pop()
solve(0)