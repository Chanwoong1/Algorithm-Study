'''
https://programmers.co.kr/learn/courses/30/lessons/72411
'''

from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        sorted_candidates = Counter(candidates).most_common()
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
    return sorted(answer)

'''
itertools 라이브러리의 combinations를 사용하여 손쉽게 조합을 구할 수 있다.
이를 이용해 orders의 메뉴들을 하나씩 불러서 k개만 사용하는 조합을 구할 수 있다.
이것으로 candidates를 채워, Counter를 이용해 candidates 리스트 내부의 요소 수를 구할 수 있다.
most_common()을 이용하면 최빈값을 찾아주면서 동시에 정렬이 가능하다.
그리고 정렬된 값의 맨 앞 값은 최빈값으로, sorted_candidates[0][1]인 값과 같은 메뉴들을 찾아 answer에 해주고 반환하면 된다.
'''