s = input()
score = 0
du = False
for i in range(1, len(s), 2) :
    c = s[i - 1]
    d = int(s[i])
    if c == 'A' : score += d
    else : score -= d
if score > 0 : print("A")
else : print("B")
