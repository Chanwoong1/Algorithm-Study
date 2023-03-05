alpha = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = input()
idx = 0
while idx < len(s) :
    print(s[idx], end = "")
    idx += alpha.index(s[idx])
