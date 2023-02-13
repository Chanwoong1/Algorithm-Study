// 영식이와 친구들
// https://www.acmicpc.net/problem/1592

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int N, M, L;
    cin >> N >> M >> L;
    int Arr[N];
    int ball = 0, cnt = 0;
    memset(Arr, 0, sizeof(int) * N);
    Arr[0] = 1;
    while (1) {
        if (Arr[ball] == M)
            break;
        ball += L;
        if (ball >= N)
            ball -= N;
        Arr[ball]++;
        cnt++;
    }
    cout << cnt;
}
