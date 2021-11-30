'''
https://programmers.co.kr/learn/courses/30/lessons/12940
'''

def solution(n, m):
    answer = []
    if n == 1 or m == 1 :
        return [1, n * m]
    else :
        # 최대공약수
        s = 1
        result1 = []
        while s <= n :
            if n % s == 0 and m % s == 0 :
                result1.append(s)
            s += 1
        answer.append(max(result1))

        # 최소공배수
        answer.append(n * m / max(result1))
        return answer