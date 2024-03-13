#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

#define fast                        \
  ios_base::sync_with_stdio(false); \
  cin.tie(0), cout.tie(0)
#define ll long long

int main() {
  fast;
  int n, s;
  cin >> n >> s;
  vector<int> v(n);
  for (int i = 0; i < n; i++) {
    cin >> v[i];
    v[i] *= s;
  }
  sort(v.rbegin(), v.rend());
  int a = v[0];
  cout << (a % 1000 ? a / 1000 + 1 : a / 1000);
}
