// 좋은 자동차 번호판
// https://www.acmicpc.net/problem/1871

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
    int N;
    cin >> N;
    for (int i = 0; i < N; ++i) {
        string Car;
        cin >> Car;
        int alpha = ((Car[0] - 'A') * 26 * 26) + ((Car[1] - 'A') * 26) + (Car[2] - 'A');
        int num = stoi(Car.substr(4, 4));
        (abs(alpha - num) <= 100) ? cout << "nice\n" : cout << "not nice\n";
    }
    return 0;
}
