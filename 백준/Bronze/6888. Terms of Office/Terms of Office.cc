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
    int x, y;
    cin >> x >> y;
    for (int i = x; i <= y; i += 60) cout << "All positions change in year " << i << "\n";
}
