// 새
// https://www.acmicpc.net/problem/1568

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    long long N;
    cin >> N;
    long long k = 1;
    int cnt = 0;
    while (N > 0) {
        if (k <= N) {
            N -= k;
            k++;
        } else {
            k = 1;
            N -= k;
            k++;
        }
        cnt++;
    }
    cout << cnt;
}
