#include <string>
#include <vector>

using namespace std;
#include <iostream>
string solution(string X, string Y) {
    string answer = "";
    vector<int> vx(10, 0);
    vector<int> vy(10, 0);
    for (int i = 0; i < X.length(); i++) vx[X[i] - '0']++;
    for (int i = 0; i < Y.length(); i++) vy[Y[i] - '0']++;
    vector<int> ans(10, 0);
    for (int i = 0; i < 10; i++) ans[i] = min(vx[i], vy[i]);
    for (int i = 9; i >= 0; i--) {
        if (ans[i] != 0) {
            for (int j = 0; j < ans[i]; j++) answer += to_string(i);
        }
    }
    return (answer.length() == 0) ? "-1" : (answer[0] == '0') ? "0" : answer;
}