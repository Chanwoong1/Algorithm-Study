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
    vector<int> v;
    for (int i = 0; i < 3; i++) {
        cin >> n;
        v.push_back(n);
    }
    sort(v.begin(), v.end());
    cout << v[1];
}
