#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    for (int i = 0; i < s.length(); i++) {
        int n = 1, m = 0, j = 1;
        while (n != m) {
            if (s[i] == s[i + j]) n++;
            else m++;
            j++;
        }
        answer++;
        i += j - 1;
    }
    return answer;
}