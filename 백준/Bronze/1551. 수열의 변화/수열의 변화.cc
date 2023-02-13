// 수열의 변화
// https://www.acmicpc.net/problem/1551

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <sstream>

using namespace std;

int N, K;
int Arr[21];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> K;
    string arr;
    cin >> arr;
    istringstream ss(arr);
    int i = 0;
    string buf;
    while (getline(ss, buf, ',')) {
        Arr[i] = stoi(buf);
        i++;
    }
    while (K > 0) {
        for (i = 0; i < N - 1; i++) {
            Arr[i] = Arr[i + 1] - Arr[i];
        }
        N--;
        K--;
    }
    for (i = 0; i < N - 1; i++) {
        cout << Arr[i] << ",";
    }
    cout << Arr[N - 1];
}
