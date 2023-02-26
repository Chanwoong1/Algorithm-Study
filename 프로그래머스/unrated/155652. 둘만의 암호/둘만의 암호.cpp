#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s, string skip, int index) {
    string answer = "";
    string alpha = "abcdefghijklmnopqrstuvwxyz";
    for (int i = 0; i < skip.length(); i++) alpha.erase(find(alpha.begin(), alpha.end(), skip[i]));
    for (int i = 0; i < s.length(); i++) {
        int change = alpha.find(s[i]) + index;
        while (change >= alpha.length()) change -= alpha.length();
        answer += alpha[change];
    }
    return answer;
}