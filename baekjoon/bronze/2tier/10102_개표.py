# https://www.acmicpc.net/problem/10102

V = int(input())
A = 0
for i in input() :
    if i == 'A' :
        A += 1
if V - A < A :
    print("A")
elif V - A == A :
    print("Tie")
else :
    print("B")