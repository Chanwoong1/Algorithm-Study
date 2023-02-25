def solution(s):
    answer = 0
    i = 0
    while i < len(s) :
        n = 1
        m = 0
        j = 1
        while n != m and i + j < len(s) :
            if s[i] == s[i + j] :
                n += 1
            else :
                m += 1
            j += 1
        answer += 1
        i += j
    return answer

    # for (int i = 0; i < s.length(); i++) {
    #     int n = 1, m = 0, j = 1;
    #     while (n != m) {
    #         if (s[i] == s[i + j]) n++;
    #         else m++;
    #         j++;
    #     }
    #     answer++;
    #     i += j - 1;
    # }
    # return answer;
