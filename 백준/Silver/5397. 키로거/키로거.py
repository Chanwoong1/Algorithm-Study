from collections import deque

for _ in range(int(input())):
    s = input()
    front = deque()
    back = deque()
    idx = 0
    ans = ""
    for i in range(len(s)):
        if s[i] == "<":
            if len(front) != 0:
                back.appendleft(front.pop())
        elif s[i] == ">":
            if len(back) != 0:
                front.append(back.popleft())
        elif s[i] == "-":
            if len(front) != 0:
                front.pop()
        else:
            front.append(s[i])
    print("".join(front) + "".join(back))
