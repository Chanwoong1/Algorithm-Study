n = int(input())
s = input()
idx = 0
hidden = 0
while idx < len(s) :
    if s[idx] >= '0' and s[idx] <= '9' :
        jdx = 0
        while idx + jdx < len(s) and s[idx + jdx] >= '0' and s[idx + jdx] <= '9' : jdx += 1
        if jdx < 7 :
            hidden += int(s[idx : idx + jdx])
        idx += jdx
    idx += 1
print(hidden)
