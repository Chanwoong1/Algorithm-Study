# https://www.acmicpc.net/problem/6764

lst = [int(input()) for _ in range(4)] 
R = 0
for i in range(3):
    if lst[i+1] > lst[i]:
        R = R + 1
    elif lst[i+1] < lst[i]:
        R = R - 1

if len(set(lst)) == 1: 
    print("Fish At Constant Depth")
elif R == 3:
    print("Fish Rising")
elif R == -3:    
    print("Fish Diving")
else:
    print("No Fish")