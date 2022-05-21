# https://www.acmicpc.net/problem/2529

N = int(input())
sign = list(input().split())

result = []
answer = []
def solve(step) :
    if step == N + 1 :
        tmp = [str(i) for i in answer]
        result.append(''.join(tmp))
        return

    for i in range(10) :
        if len(answer) == 0 :
            answer.append(i)
            solve(step + 1)
            answer.pop()
        else :
            if sign[step - 1] == '<' and i not in answer and i > answer[-1] :
                answer.append(i)
                solve(step + 1)
                answer.pop()
            elif sign[step - 1] == '>' and i not in answer and i < answer[-1] :
                answer.append(i)
                solve(step + 1)
                answer.pop()
solve(0)
print(max(result))
print(min(result))