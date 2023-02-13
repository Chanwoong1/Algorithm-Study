// 새
// https://www.acmicpc.net/problem/1568

#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    long long N, k = 1;
    cin >> N;
    int cnt = 0;
    while (N > 0) {
        if (k > N)
            k = 1;
        N -= k;
        k++, cnt++;
    }
    cout << cnt;
}
