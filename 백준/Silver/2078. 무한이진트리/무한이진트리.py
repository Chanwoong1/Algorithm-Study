A, B = map(int, input().split())
left, right = 0, 0
while A > 1 and B > 1 :
    if A > B :
        left += A // B
        A %= B
    else :
        right += B // A
        B %= A
left += A - 1
right += B - 1
print(left, right)