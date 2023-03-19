import sys
input = sys.stdin.readline

def get_divs(n) :
    return [i for i in range(1, n) if n%i == 0]

while True :
    s = list(map(int, input().split()))
    i = 0
    while i < len(s) :
        temp = s[i]
        if temp == 0:
            exit(0)
        hap = sum(get_divs(temp))
        if hap < temp :
            print(str(temp), "DEFICIENT")
        elif hap == temp :
            print(str(temp), "PERFECT")
        elif hap > temp :
            print(str(temp), "ABUNDANT")

        i += 1
