// 완전제곱수
// https://www.acmicpc.net/problem/1977

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
    int M, N;
    cin >> M >> N;
    int ans = 0;
    int m;
    for (int i = 0; i <= 100; ++i) {
        if (ans == 0 && i * i >= M && i * i <= N) m = i * i;
        if (i * i >= M && i * i <= N) ans += i * i;
    }
    if (ans == 0) cout << -1;
    else cout << ans << "\n" << m;
    return 0;
}
