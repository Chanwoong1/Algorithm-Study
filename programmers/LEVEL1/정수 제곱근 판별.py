'''
https://programmers.co.kr/learn/courses/30/lessons/12934
'''

def solution(n):
    if (n ** 0.5) == round(n ** 0.5) :  # n의 제곱근과 n의 제곱근의 round값이 같다는 것은 정수형이라는 뜻
        x = n ** 0.5                    # 조건에 따라 x 추가
        return (x + 1) ** 2             # x + 1의 제곱 반환
    else :
        return -1                       # 나머지 경우 -1 반환