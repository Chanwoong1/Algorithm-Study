'''
https://programmers.co.kr/learn/courses/30/lessons/12921
'''

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5)+1):   # 제곱근을 해줌으로써 시간복잡도를 줄일 수 있다.
            if num%i == 0:
                return False
        return True

def solution(n):
    answer = 0
    for i in range(2, n + 1) :
        answer += isPrime(i)
    return answer