// 2진수 8진수
// https://www.acmicpc.net/problem/1373

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

void convert2To8(string a) {
    int len = a.length();
    int i = 0;
    if (len % 3 == 1) {
        cout << a[0];
        i = 1;
    } else if (len % 3 == 2) {
        cout << ((a[0] - '0') * 2) + (a[1] - '0');
        i = 2;
    }
    for (; i < len; i += 3)
        cout << ((a[i] - '0') * 4) + ((a[i + 1] - '0') * 2) + (a[i + 2] - '0');
}

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    string a;
    cin >> a;
    convert2To8(a);
    return 0;
}
