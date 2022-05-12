'''문제
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

입력
첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

제한
1 ≤ N ≤ 1,000,000
-109 ≤ Xi ≤ 109
'''

# 시간초과
import sys
N = int(sys.stdin.readline())
X = list(sys.stdin.readline().split())
num_dict = {}
sorted_X = sorted([int(i) for i in X])

n = 0
for i in range(len(sorted_X) - 1) :
    if sorted_X[i] != sorted_X[i+1] :
        num_dict[str(sorted_X[i])] = n
        n += 1
    else :
        num_dict[str(sorted_X[i])] = n

result = []
for i in X :
    result.append([v for j, v in num_dict.items() if j == i][0])

print(' '.join([str(i) for i in result]))

# 수정
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end = ' ')