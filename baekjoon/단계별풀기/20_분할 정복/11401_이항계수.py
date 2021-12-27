# https://www.acmicpc.net/problem/11401

def power(a, b):
    if b == 1: # b의 값이 1이면 a % C를 return한다.
        return a * 2 % 1000000007
    else:
        temp = power(a, b - 1) # a^(b // 2)를 미리 구한다.
        # if b % 2 == 0:
        #     return temp * temp % 1000000007 # b가 짝수인 경우
        # else:
        #     return temp * temp * a % 1000000007 # b가 홀수인 경우
        return temp % 1000000007

N, K = map(int, input().split())
print(power(N, K))