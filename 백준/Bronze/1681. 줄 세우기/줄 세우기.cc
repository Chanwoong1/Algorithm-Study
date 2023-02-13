// 줄 세우기
// https://www.acmicpc.net/problem/1681

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int N, L, c = 1;

bool f(int a, int b) {
    string s = to_string(a);
    for (int i = 0; i < s.length(); ++i) {
        if (s[i] == (b + '0'))
            return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> L;
    while (N) {
        if (f(c, L))
            N--;
        c++;
    }
    cout << c - 1;
    return 0;
}
