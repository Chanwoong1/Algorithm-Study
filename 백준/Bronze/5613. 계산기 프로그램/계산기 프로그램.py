ans = int(input())
while True :
    op = input()
    if op == '+' : ans += int(input())
    elif op == '-' : ans -= int(input())
    elif op == '*' : ans *= int(input())
    elif op == '/' : ans //= int(input())
    else : break
print(ans)
