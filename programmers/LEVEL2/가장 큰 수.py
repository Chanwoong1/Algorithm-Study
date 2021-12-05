'''
https://programmers.co.kr/learn/courses/30/lessons/42746#
'''

# 첫 시도
from itertools import permutations

def sort_num(numbers) :
    dict = {str(x) : [] for x in range(9, -1, -1)}
    for i in numbers :
        dict[str(i)[0]].append(str(i))
    return dict

def find_num(dict) :
    answer = ''
    for i in range(9, -1, -1) :
        if dict[str(i)] != [] :
            if i == 0 :
                answer += ''.join(dict[str(i)])
            else :
                answer += str(max([int(i) for i in list(map(''.join, permutations(dict[str(i)])))]))
    return str(int(answer))


def solution(numbers):
    dict = sort_num(numbers)
    return find_num(dict)

## 위의 코드는 몇개의 문항에서 시간초과가 나왔다 ...

# 수정
def solution(numbers):
    #0. key point
    numbers_str = [str(num) for num in numbers]                 #1. 사전 값으로 정렬하기
    numbers_str.sort(key=lambda num: num*3, reverse=True)       #2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교

    return str(int(''.join(numbers_str)))
    # 만약 numbers=[0,0,0,0] 이라면 0 이 나와야 한다.
    # join한 값을 int로 만들어 준 후 원하는 return값이 str이기 때문에 다시 str로 변환한다.