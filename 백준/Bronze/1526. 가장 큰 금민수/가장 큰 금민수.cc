// 가장 큰 금민수
// https://www.acmicpc.net/problem/1526

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int N;
    cin >> N;
    while (N > 0) {
        string tmp = to_string(N);
        for (int i = 0; i < tmp.length(); i++) {
            if (tmp[i] != '7' && tmp[i] != '4')
                break;
            if (i == tmp.length() - 1) {
                cout << N;
                return 0;
            }
        }
        --N;
    }
    return 0;
}
