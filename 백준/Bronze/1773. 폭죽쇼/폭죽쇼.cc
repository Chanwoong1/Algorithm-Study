// 폭죽쇼
// https://www.acmicpc.net/problem/1773

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;
int N, C, cnt = 0, idx = 1;
int Arr[101];
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> C;
    bool a = false;
    for (int i = 0; i < N; ++i)
        cin >> Arr[i];
    while (idx <= C) {
        for (int i = 0; i < N; ++i)
            if (idx % Arr[i] == 0)
                a = true;
        if (a)
            cnt++;
        idx++;
        a = false;
    }
    cout << cnt;
    return 0;
}
