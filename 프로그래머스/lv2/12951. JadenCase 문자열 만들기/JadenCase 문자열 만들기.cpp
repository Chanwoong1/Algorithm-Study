#include <string>
#include <vector>

using namespace std;

int isalpha(char c) {
    return ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) ? ((c >= 'a' && c <= 'z') ? 1 : 2) : 0; 
}


string solution(string s) {
    string answer = "";
    if (isalpha(s[0]) == 1) answer += s[0] - 32;
    else answer += s[0];
    for (int i = 1; i < s.length(); i++) {
        if (s[i - 1] == ' ' && isalpha(s[i]) == 1) answer += s[i] - 32;
        else if (s[i - 1] == ' ' && isalpha(s[i]) != 1) answer += s[i];
        else {
            if (s[i] >= 'A' && s[i] <= 'Z') answer += s[i] + 32;
            else answer += s[i];
        }
    }
    return answer;
}