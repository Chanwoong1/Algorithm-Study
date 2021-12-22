# https://www.acmicpc.net/problem/3036

def getGCD(a, b) :
    r = a % b
    while r != 0 :
        a = b
        b = r
        r = a % b
    return b

int(input())    # 필요없음
lst = list(map(int, input().split()))
first = lst.pop(0)  # 초기값 설정
for i in lst :
    if first % i == 0 :     # 분모가 1인 경우
        print(str(first//i) + '/1')
    else :
        if first > i :      # 나머지 경우 최대공약수를 구해준다
            a = getGCD(i, first)
            print(str(first // a) + '/' + str(i // a))
        else :
            a = getGCD(first, i)
            print(str(first // a) + '/' + str(i // a))
