'''
https://programmers.co.kr/learn/courses/30/lessons/1845
'''

def solution(nums):
    maxi = len(nums) // 2   # 최대 N / 2마리 가져갈 수 있음
    num_lst = [0] * (max(nums) + 1) # 딕셔너리의 역할
    for i in nums :     # 각 nums 별로 딕셔너리에 추가
        num_lst[i] += 1
    answer = len([i for i in num_lst if i != 0])    # 0을 제외하면 폰켓몬 종류의 수를 출력할 수 있다.
    if answer > maxi :
        answer = maxi
    return answer