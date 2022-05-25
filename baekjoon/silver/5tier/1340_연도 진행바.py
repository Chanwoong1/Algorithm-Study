# https://www.acmicpc.net/problem/1340

d = list(input().split())
month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for i in range(len(month_lst)) :
    if d[0] == month_lst[i] :
        month = i + 1
day = int(d[1][:-1])
year = int(d[2])
hh, mm = map(int, d[3].split(':'))
month_day_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) :
    month_day_lst[1] += 1
total = sum(month_day_lst) * 24 * 60

current = (sum(month_day_lst[ : month - 1]) + day - 1) * 24 * 60 + hh * 60 + mm
print(current / total * 100)