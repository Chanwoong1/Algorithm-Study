#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    for (int i = 0; i < t.length() - p.length() + 1; i++) {
        long long a = stoll(t.substr(i, p.length())), b = stoll(p);
        if (a <= b) answer++;
    }
    return answer;
}