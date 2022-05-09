# https://www.acmicpc.net/problem/5355

for _ in range(int(input())) :
    lst = list(input().split())
    answer = float(lst.pop(0))
    while (lst) :
        tmp = lst.pop(0)
        if tmp == '@' :
            answer *= 3
        elif tmp == '%' :
            answer += 5
        else :
            answer -= 7
    print(f"{answer:.2f}")