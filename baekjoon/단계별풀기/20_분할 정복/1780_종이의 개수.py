# https://www.acmicpc.net/problem/1780

# 2630_색종이 만들기에 코드 추가
import sys
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 
result = []

def solution(x, y, N) :
    p = paper[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if p != paper[i][j] :
                # 9분할
                solution(x, y, N//3)
                solution(x, y+N//3, N//3)
                solution(x, y+2*(N//3), N//3)
                solution(x+N//3, y, N//3)
                solution(x+N//3, y+N//3, N//3)
                solution(x+N//3, y+2*(N//3), N//3)
                solution(x+2*(N//3), y, N//3)
                solution(x+2*(N//3), y+N//3, N//3)
                solution(x+2*(N//3), y+2*(N//3), N//3)
                return
    if p == 0 :
        result.append(0)
    elif p == 1 :
        result.append(1)
    else :
        result.append(-1)

solution(0, 0, N)
print(result.count(-1))
print(result.count(0))
print(result.count(1))