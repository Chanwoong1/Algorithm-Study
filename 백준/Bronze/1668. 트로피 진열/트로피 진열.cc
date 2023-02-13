// 트로피 진열
// https://www.acmicpc.net/problem/1668

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;
int N;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    int Arr[N];
    for (int i = 0; i < N; i++)
        cin >> Arr[i];
    int l = 0, r = 0, lc = 0, rc = 0;
    for (int i = 0; i < N; i++) {
        if (l < Arr[i]) {
            l = Arr[i];
            lc++;
        }
    }
    for (int i = N - 1; i > -1; i--) {
        if (r < Arr[i]) {
            r = Arr[i];
            rc++;
        }
    }
    cout << lc << "\n" << rc;
    return 0;
}
