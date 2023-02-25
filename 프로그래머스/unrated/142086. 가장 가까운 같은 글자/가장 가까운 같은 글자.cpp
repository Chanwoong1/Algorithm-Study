#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    for (int i = 0; i < s.length(); i++) {
        bool first = true;
        for (int j = i - 1; j > -1; j--) {
            if (s[i] == s[j]) {
                first = false;
                answer.push_back(i - j);
                break;
            }
        }
        if (first) answer.push_back(-1);
    }
    return answer;
}