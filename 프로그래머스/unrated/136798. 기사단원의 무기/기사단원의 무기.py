def get_power(num):
    cnt = 0
    for i in range(1, int(num ** (0.5)) + 1):
        if num % i == 0:
            cnt += 1
            if (i ** 2 != num) :
                cnt += 1
    return cnt

def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        k = get_power(i)
        answer += k if k <= limit else power
    return answer