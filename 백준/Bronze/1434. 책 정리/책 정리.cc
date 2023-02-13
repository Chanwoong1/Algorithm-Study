// 책 정리
// https://www.acmicpc.net/problem/1434

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int N, M;
int Boxes[51];
int Books[51];

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    for (int i = 0; i < N; ++i) {
        cin >> Boxes[i];
    }
    for (int i = 0; i < M; ++i) {
        cin >> Books[i];
    }
    int ans = 0;
    int idx = 0;
    for (int i = 0; i < M; ++i) {
        while (1) {
            if (Books[i] <= Boxes[idx]) {
                Boxes[idx] -= Books[i];
                break;
            } else {
                ans += Boxes[idx];
                ++idx;
            }
        }
    }
    for (; idx < N; ++idx) {
        ans += Boxes[idx];
    }
    cout << ans;
    return 0;
}
