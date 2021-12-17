# https://www.acmicpc.net/problem/11054


# 시간 초과
N = int(input())
lst = list(map(int, input().split()))

bt_dict = {}
for k in range(N - 1) :
    dp = [lst[k]]
    for i in range(k + 1, N) :
        if dp[-1] > lst[i] :
            dp.append(lst[i])
        else :
            idx = 0
            for j in range(len(dp)) :
                if dp[j] > lst[i] :
                    idx += 1
                elif idx == 0 :
                    if dp[idx] > lst[i] :
                        dp.insert(idx + 1, lst[i])
                else :
                    dp[idx] = lst[i]
                    break

    bt_dict[k] = len(dp)

    dp = [lst[0]]
    for i in range(0, k + 1) :
        if dp[-1] < lst[i] :
            dp.append(lst[i])
        else :
            idx = 0
            for j in range(len(dp)) :
                if dp[j] < lst[i] :
                    idx += 1
                else :
                    dp[idx] = lst[i]
                    break
    bt_dict[k] += (len(dp) - 1)
                
print(sorted(bt_dict.items(), key = lambda x : x[1], reverse = True)[0][1])

# 수정

x = int(input())

lst = list(map(int, input().split()))
reverse_lst = case[::-1]

increase = [1 for i in range(x)] # 가장 긴 증가하는 부분 수열
decrease = [1 for i in range(x)] # 가장 긴 감소하는 부분 수열(reversed)

for i in range(x):
    for j in range(i):
        if lst[i] > lst[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_lst[i] > reverse_lst[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for i in range(x)]
for i in range(x):
    result[i] = increase[i] + decrease[x-i-1] -1

print(max(result))
