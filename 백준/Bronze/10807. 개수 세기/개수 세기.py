input()
lst = list(map(int, input().split()))
n = int(input())
print(sum([1 for i in lst if i == n]))