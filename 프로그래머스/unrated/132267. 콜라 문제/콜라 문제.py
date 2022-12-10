def solution(a, b, n):
    answer = 0
    while n >= a :
        div, mod = divmod(n, a)
        answer += b * div
        n = b * div + mod
    return answer