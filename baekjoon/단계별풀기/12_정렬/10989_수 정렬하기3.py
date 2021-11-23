'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''
# 시간초과
import sys

result = []
for _ in range(int(input())) :
    result.append(int(sys.stdin.readline()))
result.sort()
for i in result :
    print(i)

## 수정
import sys
check_list = [0] * 10001
for i in range(int(input())) :  # 입력받기
    input_num= int(sys.stdin.readline())    # 수를 입력받으면
    check_list[input_num - 1] = check_list[input_num - 1] + 1   # 리스트에서 수에 해당하는 위치 +1

for i in range(10001) : # 출력
    if check_list[i] != 0 :
        for j in range(check_list[i]) :
            print(i + 1)