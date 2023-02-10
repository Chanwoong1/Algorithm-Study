from itertools import combinations, permutations

import sys
input = sys.stdin.readline
prime = [True] * 10000001
prime[0] = prime[1] = False
for i in range(int(10000000 ** 0.5) + 1) :
    if prime[i] :
        for j in range(2 * i, 10000001, i) :
            prime[j] = False

for _ in range(int(input())) :
    n = list(input().replace("\n", ""))
    answer = set()
    for i in range(1, len(n) + 1) :
        for comb in combinations(n, i) :
            for perm in permutations(comb, i) :
                if prime[int(''.join(perm))] :
                    answer.add(int(''.join(perm)))
    print(len(answer))
