// 자기복제수
// https://www.acmicpc.net/problem/2028

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
    int T, N;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        string tmp = to_string(N * N);
        if (N == stoi(tmp.substr(tmp.length() - to_string(N).length(), to_string(N).length()))) cout << "YES\n";
        else cout << "NO\n";
    }
}
