# https://www.acmicpc.net/problem/11478

str = input()
lst = []
for i in range(len(str)) :
    for j in range(i + 1, len(str) + 1) :
        lst.append(str[i : j])
print(len(set(lst)))