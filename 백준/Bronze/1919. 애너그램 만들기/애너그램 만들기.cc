// 애너그램 만들기
// https://www.acmicpc.net/problem/1919

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
    string a, b;
    cin >> a >> b;
    int aa[26], bb[26], ans = 0;
    memset(aa, 0, sizeof(int) * 26);
    memset(bb, 0, sizeof(int) * 26);
    for (int i = 0; i < a.length(); ++i) aa[a[i] - 'a']++;
    for (int i = 0; i < b.length(); ++i) bb[b[i] - 'a']++;
    for (int i = 0; i < 26; ++i) (aa[i] > bb[i]) ? ans += bb[i] : ans += aa[i];
    cout << a.length() + b.length() - 2 * ans;
    return 0;
}
