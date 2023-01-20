prime = [True] * 1000001
prime[0] = prime[1] = False
for i in range(1000001) :
    if prime[i] :
        for j in range(2 * i, 1000001, i) :
            prime[j] = False
for _ in range(int(input())) :
    gold = int(input())
    answer = 0
    for i in range(2, (gold // 2) + 1) :
        if prime[i] and prime[gold - i] :
            answer += 1
    print(answer)