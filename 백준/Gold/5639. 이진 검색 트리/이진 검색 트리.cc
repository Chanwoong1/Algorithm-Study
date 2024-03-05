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
  vector<int> v;
  int x;
  while (1) {
    cin >> x;
    if (cin.eof()) break;
    v.push_back(x);
  }
  function<void(int, int)> dfs = [&](int start, int end) {
    if (start == end) return;
    int root = v[start];
    int idx = start + 1;
    while (idx < end && v[idx] < root) idx++;
    dfs(start + 1, idx);
    dfs(idx, end);
    cout << root << '\n';
  };
  dfs(0, v.size());
}
