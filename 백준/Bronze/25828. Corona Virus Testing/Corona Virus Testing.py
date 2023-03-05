g, p, t = map(int, input().split())
if p * g < g + (p * t) : print(1)
elif p * g > g + (p * t) : print(2)
else : print(0)
