// 암호
// https://www.acmicpc.net/problem/1855

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define fast ios_base::sync_with_stdio(false); cin.tie(0), cout.tie(0)
#define ll long long

int main() {
    fast;
    int n;
    int c = 0;
    int rem;
    int cycle;
    bool flag = false;
    char map[20][200];
    string s;
    string result = "";

    cin >> n;
    cin >> s;

    memset(map, ' ', sizeof(map));
    cycle = (s.length() + n - 1) / n;

    for (int i = 0; i < cycle; ++i) {
        if (!flag) {
            for (int j = 0; j < n; ++j) {
                map[i][j] = s[c++];
            }
        }
        else {
            for (int j = n - 1; j >= 0; --j) {
                map[i][j] = s[c++];
            }
        }
        flag = !flag;
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < cycle; ++j) {
            result += map[j][i];
        }
    }

    cout << result << endl;

    return 0;
}