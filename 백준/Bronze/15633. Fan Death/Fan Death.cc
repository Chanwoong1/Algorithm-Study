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
    int n; cin >> n;
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) sum += i;
    }
    cout << sum * 5 - 24;
}