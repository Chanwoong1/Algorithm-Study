check = set([i for i in range(1, 31)])
for _ in range(28) :
    check.discard(int(input()))
print(list(check)[0])
print(list(check)[1])