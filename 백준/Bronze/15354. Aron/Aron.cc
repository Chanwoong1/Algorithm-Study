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
  int N;
  cin >> N;
  vector<char> v(N);
  for (int i = 0; i < N; i++) cin >> v[i];
  int ans = 2;
  for (int i = 1; i < N; i++)
    if (v[i] != v[i - 1]) ans++;
  cout << ans << "\n";
}
