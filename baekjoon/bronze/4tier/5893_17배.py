# https://www.acmicpc.net/problem/5893

# 2진수를 10진수로 변환 후 17배
n = int(input(), 2) * 17
# 2진수로 출력
print(bin(n)[2:])