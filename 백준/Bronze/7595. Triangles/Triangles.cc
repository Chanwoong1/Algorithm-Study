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
    int n;
    while (1) {
        cin >> n;
        if (n == 0) break;
        for (int i = 1; i < n + 1; i++) {
            for (int j = 0; j < i; j++) {
                cout << "*";
            }
            cout << "\n";
        }
    }
}
