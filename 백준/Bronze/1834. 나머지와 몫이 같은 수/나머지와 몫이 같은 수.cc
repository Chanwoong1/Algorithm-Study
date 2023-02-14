// 나머지와 몫이 같은 수
// https://www.acmicpc.net/problem/1834

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
    int N;
    cin >> N;
    ll ans = 0;
    for (ll i = 1; i < N; ++i)
        ans += i * (N + 1);
    cout << ans;
    return 0;
}
