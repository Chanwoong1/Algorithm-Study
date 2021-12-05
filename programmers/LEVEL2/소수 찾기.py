'''
https://programmers.co.kr/learn/courses/30/lessons/42839
'''

from itertools import permutations
from collections import Counter
def solution(numbers):
    numbers = [str(i) for i in numbers]
    primes = []
    for i in range(1, len(numbers) + 1) :
        primes += Counter([int(''.join(j)) for j in permutations(numbers, i)])
    primes = list(Counter(primes))
    if 0 in primes :
        primes.remove(0)
    if 1 in primes :
        primes.remove(1)
        
    answer = len(primes)
    for i in primes :
        for j in range(2 , i) :
            if i % j == 0 :
                answer -= 1
                break
    return answer

'''
문자형으로 변환한 numbers의 요소들을 리스트 형태로 변환
하나만 뽑히는 상황부터, numbers 리스트 전체가 뽑히는 상황까지를 고려한 for문으로 순열 조합을 만들어줌
Counter를 사용하면 요소들을 손쉽게 primes라는 빈 리스트에 추가해줄 수 있다.

primes에 Counter를 한번 더 사용하면 중복이 제거된다. list형태를 다시 취해주는건 key값만 사용할 것이기 때문.
0과 1은 소수를 찾는것에 쓸모 없으니 제거
나머지 primes에 들어있는 값들의 수를 answer로 놓고 시작
하나씩 소수를 찾아가면서 소수가 아닌것들을 발견할 때마다 answer를 1씩 줄여준다.
최종 answer 반환
'''