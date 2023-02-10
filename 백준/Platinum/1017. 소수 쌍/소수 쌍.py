def dfs(x):
    global Y
    global matched
    global visited
    if visited[Y.index(x)] :
        return False
    visited[Y.index(x)] = True
    for y in Y :
        if x + y in primes:
            if y not in matched or dfs(matched[y]) :
                matched[y] = x
                return True
    return False

N = int(input())
lst = list(map(int, input().split()))
prime = [True] * 2001
prime[0] = prime[1] = False
for i in range(2, int(2000 ** 0.5) + 1) :
    if prime[i] :
        for j in range(2 * i, 2001, i) :
            prime[j] = False
primes = [i for i in range(2001) if prime[i]]
answers = []
for i in lst :
    matched = {}
    if i == lst[0] :
        continue
    if lst[0] + i in primes :
        if N == 2 :
            answers.append(i)
            break
        Y = [j for j in lst]
        del Y[0]
        del Y[Y.index(i)]
        matched = {}
        for y in Y :
            visited = [False for _ in range(len(Y))]
            dfs(y)
    if N != 2 and len(matched) == N - 2 :
        answers.append(i)
if not answers :
    answers.append(-1)
answers.sort()
print(' '.join(list(map(str, answers))))