# https://www.acmicpc.net/problem/1543

doc = input()
find_doc = input()
i = 0
answer = 0
while i <= len(doc) - len(find_doc) :
    if doc[i : i + len(find_doc)] == find_doc :
        answer += 1
        i += len(find_doc)
    else :
        i += 1
print(answer)