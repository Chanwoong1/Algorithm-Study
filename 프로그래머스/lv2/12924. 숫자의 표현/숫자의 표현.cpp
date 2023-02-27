#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n) {
    int answer = 0;
    vector<int> dp(n + 1, 0);
    dp[1] = 1;
    for (int i = 2; i < n + 1; i++) {
        dp[i] = dp[i - 1] + i;
    }
    // for (int i = 0; i < n + 1; i++) cout << dp[i] << " ";
    // cout << "\n";
    int start = 1, end = 0;
    while (start <= n) {
        // cout << start << ", " << end << " : " << dp[start] - dp[end] << "\n";
        if (dp[start] - dp[end] > n) end++;
        else if (dp[start] - dp[end] < n) start++;
        else {
            answer++;
            start++;
        }
    }
    return answer;
}
