// 추론
// https://www.acmicpc.net/problem/1731

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int N;
int Arr[51];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for (int i = 0; i < N; ++i)
        cin >> Arr[i];
    if (Arr[1] - Arr[0] == Arr[2] - Arr[1])
        cout << Arr[N - 1] + Arr[1] - Arr[0];
    else
        cout << Arr[N - 1] * (Arr[1] / Arr[0]);
    return 0;
}
