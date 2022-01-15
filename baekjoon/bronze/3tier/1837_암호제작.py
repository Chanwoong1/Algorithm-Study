# https://www.acmicpc.net/problem/1837

P, K = map(int, input().split())

# K보다 작은 소수들 구하기 (에라토스테네스의 체)
K -= 1                                  # K보다 작기 때문에 1을 뺀다
a = [False, False] + [True] * (K - 1)
prime = []
for i in range(2, K + 1):
    if a[i]:
        prime.append(i)
        for j in range(2 * i, K + 1, i):
            a[j] = False

result = 'GOOD'
for item in prime:              # K보다 작은 소수들 중에서 (작은 소수부터 차례로)
    if P % item == 0:           # 나누어 떨어지면 반복문 종료
        result = f'BAD {item}'
        break
print(result)