# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())

lst = [int(input()) for _ in range(N)]

num = 0
while K > 0 :
    tmp = lst.pop()     # 동전의 가치가 큰것부터 뽑음
    if tmp <= K :       # K가 tmp보다 큰 경우
        num += (K // tmp)   # tmp의 갯수만큼 num 추가
        K = K % tmp     # 거스름돈
print(num)