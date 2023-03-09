def solution(s):
    cnt_zero = 0
    idx = 0
    while len(s) != 1 :
        s_len = sum([1 for i in s if i == "1"])
        cnt_zero += len(s) - s_len
        s = str(bin(s_len)[2:])
        idx += 1
    return [idx, cnt_zero]