'''
https://programmers.co.kr/learn/courses/30/lessons/43165#
'''

def solution(numbers, target):
    result = 0
    def dfs(num, level):
        nonlocal result

        if level == len(numbers):   # 종료조건
            if num == target:
                result += 1
            return

        signs = [-num, num]         # + 혹은 -
        if level == 1:
            for i in range(2):
                dfs(signs[i] + numbers[level], level + 1)
                dfs(signs[i] - numbers[level], level + 1)
        else:
            dfs(num + numbers[level], level + 1)
            dfs(num - numbers[level], level + 1)

    dfs(numbers[0], 1)      # 처음 시작 구간
    return result

'''
numbers = [1, 1, 1, 1, 1]
target = 3 일 경우
dfs(numbers[0], 1) 부터 시작하면 numbers의 처음인 1이 들어간다.
dfs 내부에 종료조건을 만족하지 않으므로 지나가고,
level == 1인 경우의 조건을 만족하여
i = 0
dfs(signs[i] + numbers[level], level + 1) -> dfs(-1 + 1, 2) -> dfs(0, 2) -> ...
dfs(signs[i] - numbers[level], level + 1) -> dfs(-1 - 1, 2) -> dfs(-1, 2) -> ...
i = 1
dfs(signs[i] + numbers[level], level + 1) -> dfs(1 + 1, 2) -> dfs(2, 2) -> ...
dfs(signs[i] - numbers[level], level + 1) -> dfs(1 - 1, 2) -> dfs(0, 2) -> ...

dfs(0, 2)부터는 else 조건을 만족하게 되므로
dfs(num + numbers[level], level + 1) -> dfs(0 + 1, 3) -> dfs(1, 3) -> ...
dfs(num - numbers[level], level + 1) -> dfs(0 - 1, 3) -> dfs(-1, 3) -> ...

target == 3이 될때까지 반복하면서 if num == target을 만족하는 값들을 대상으로 result += 1을 시행한다.
'''