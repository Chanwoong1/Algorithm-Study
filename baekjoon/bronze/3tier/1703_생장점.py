# https://www.acmicpc.net/problem/1703

while 1 :
    tree = list(map(int, input().split()))
    if sum(tree) == 0 :
        break

    age = tree.pop(0)
    leaf = 0
    for i in range(len(tree) // 2) :
        if i == 0 :
            branch = tree[i]
            leaf = branch - tree[i + 1]
        else :
            branch = tree[2 * i]
            leaf = leaf * branch - tree[2 * i + 1]
    print(leaf)
