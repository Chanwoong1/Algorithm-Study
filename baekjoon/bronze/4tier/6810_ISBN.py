# https://www.acmicpc.net/problem/6810

ISBN = 9*1 + 7*3 + 8*1 + 0*3 + 9*1 + 2*3 + 1*1 + 4*3 + 1*1 + 8*3
ISBN += int(input()) * 1
ISBN += int(input()) * 3
ISBN += int(input()) * 1
print('The 1-3-sum is {}'.format(ISBN))