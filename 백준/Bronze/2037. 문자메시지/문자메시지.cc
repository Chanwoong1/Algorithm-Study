// 문자메시지
// https://www.acmicpc.net/problem/2037

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define fast ios_base::sync_with_stdio(false); cin.tie(0), cout.tie(0)
#define ll long long

int main() {
    int p, w;
    int now = 0, result = 0;
    int num[2][27] = { { 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4 },
                    { 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9 } };
    string s;
    scanf("%d%d", &p, &w);
    getchar();
    getline(cin, s);
    for (int i = 0; i < s.length(); ++i) {
        int index = -1;
        if (s[i] >= 'A' && s[i] <= 'Z') index = s[i] - 'A' + 1;
        if (s[i] == ' ') index = 0;
        if (index != -1) {
            result += num[0][index] * p;
            if (now == num[1][index] && index != 0) result += w;
            now = num[1][index];
        }
    }
    cout << result << endl;
    return 0;
}
