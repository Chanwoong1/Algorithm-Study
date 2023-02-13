// 암호
// https://www.acmicpc.net/problem/1718

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    string a, b;
    getline(cin, a);
    getline(cin, b);
    int idx = 0;
    for (int i = 0; i < a.length(); ++i) {
        if (a[i] == ' ')
            cout << a[i];
        else if ((a[i] - '0') - (b[idx] - '0') <= 0)
            cout << (char)((a[i] - '0') - (b[idx] - '0') + 25 + 'a');
        else
            cout << (char)((a[i] - '0') - (b[idx] - '0') - 1 + 'a');
        (idx == b.length() - 1) ? idx = 0 : ++idx;
    }
    return 0;
}
