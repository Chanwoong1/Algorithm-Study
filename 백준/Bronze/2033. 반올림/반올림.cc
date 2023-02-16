// 반올림
// https://www.acmicpc.net/problem/2033

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
    int N, t = 0;
    cin >> N;
    while ((int)pow(10, t + 1) < N) {
        int tmp = N % (int)(pow(10, t + 1));
        (tmp >= (int)pow(10, t + 1) / 2) ? N += ((int)pow(10, t + 1) - tmp) : N -= tmp;
        t++;
    }
    cout << N;
}
