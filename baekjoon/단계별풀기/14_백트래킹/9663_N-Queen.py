'''
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
'''

# 시간초과
# def dfs(queen, n, row):
#     count = 0
    
#     if n == row:
#         return 1
    
#     # 가로로 한번만 진행
#     for col in range(n):
#         queen[row] = col

#         # for-else구문
#         for x in range(row):
#             # 세로로 겹치면 안됨
#             if queen[x] == queen[row]: 
#                 break
                
#             # 대각선으로 겹치면 안됨
#             if abs(queen[x]-queen[row]) == (row-x):
#                 break
#         else:
#             count += dfs(queen, n, row+1)
            
#     return count

# def solution(n):
#     queen = [0]*n
        
#     return dfs(queen, n, 0)
# print(solution(int(input())))

# 수정 - 시간초과
# def adjacent(x): # x와 i 가 같으면 행이 같은거 근데 for문을 보면 x와 i가 같을 수가 없다.
#     for i in range(x): #인덱스가 행  row[n]값이 열
#         if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # 열이 같거나 대각선이 같으면 false
#             return False # 대각선이 같은경우는 두 좌표에서 행 - 행 = 열 - 열 이 같으면 두개는 같은 대각선상에 있다.
#     return True
 
# #한줄씩 재귀하며 dfs 실행
 
# def dfs(x):
#     global result
 
#     if x == N:
#         result += 1
#     else:
#         # 각 행에 퀸 놓기
#         for i in range(N): # i 는 열번호 0부터 N 전까지 옮겨가면서 유망한곳 찾기
#             row[x] = i
#             if adjacent(x): # 행,열,대각선 체크함수 true이면 백트래킹 안하고 계속 진행
#                 dfs(x + 1)
 
# N = int(input())
# row = [0] * N
# result = 0
# dfs(0)
# print(result)

# 수정
n = int(input())
row = [0] * n
column = [False] * n
left_right = [False] * (2 * n - 1)
right_left = [False] * (2 * n - 1)
cnt = []

def Queen(i) :
    for j in range(n) :
        if not column[j] and not left_right[i + j] and not right_left[i - j + n - 1] :
            row[i] = j
            if i == n - 1 :
                cnt.append(row)
            else :
                column[j] = left_right[i + j] = right_left[i - j + n - 1] = True
                Queen(i + 1)
                column[j] = left_right[i + j] = right_left[i - j + n - 1] = False

Queen(0)
print(len(cnt))
