// 피시방 알바
// https://www.acmicpc.net/problem/1453

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int N;
int Cus[101];
int Comp[101];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for (int i = 1; i <= N; i++)
        cin >> Cus[i];
    memset(Comp, 0, sizeof(int) * 101);
    int ans = 0;
    for (int i = 1; i <= N; i++)
    {
        if (Comp[Cus[i]] != 0)
            ans++;
        Comp[Cus[i]] = 1;
    }
    cout << ans;
}
