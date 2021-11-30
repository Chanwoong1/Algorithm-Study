'''
https://programmers.co.kr/learn/courses/30/lessons/12969?language=python3
'''

a, b = map(int, input().strip().split(' '))

aa = '*' * a
for _ in range(b) :
    print(aa)