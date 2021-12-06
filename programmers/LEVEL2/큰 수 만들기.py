'''
https://programmers.co.kr/learn/courses/30/lessons/42883
'''

# 시간초과
# from itertools import combinations
# def solution(number, k):
#     answer = 0
#     for i in combinations(list(str(number)), len(number) - k) :
#         if int(''.join(i)) > answer :
#             answer = int(''.join(i))
#     return str(answer)

'''
combinations 함수를 쓰면 안되는것같다..
'''

# 수정
def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)
        
    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)

'''
number를 맨 첫자리부터 하나씩 반복문을 돌린다.
처음의 if문으로 answer에 없다면 추가
그 다음부터는 두번째의 if문으로 while문을 통해 비교한다.
answer의 마지막 수가 num보다 작다면 answer에서 제거하고 k를 1 줄인다.
그리고 answer에 아무것도 없어지거나 k가 0이 되면 break
'''