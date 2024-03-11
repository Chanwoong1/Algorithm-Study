#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
    float M;
    cin >> M;
    cout << fixed << setprecision(1);
    cout << max(0.0f, M - 30) + M / 2.0f;
}