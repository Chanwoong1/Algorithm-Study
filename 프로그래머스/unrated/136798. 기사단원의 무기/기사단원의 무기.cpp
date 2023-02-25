#include <string>
#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

int get_power(int num) {
    int cnt = 0;
    for (int i = 1; i < (int)(pow(num, 0.5)) + 1; i++) {
        if (num % i == 0) {
            cnt++;
            if ((int)pow(i, 2) != num)
                cnt++;
        }
    }
    return cnt;
}

int solution(int number, int limit, int power) {
    int answer = 0;
    for (int i = 1; i <= number; i++) {
        int p = get_power(i);
        (p > limit) ? answer += power : answer += p;
    }
    return answer;
}