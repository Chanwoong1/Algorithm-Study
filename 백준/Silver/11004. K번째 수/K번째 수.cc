#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <vector>

using namespace std;

#define fast                        \
  ios_base::sync_with_stdio(false); \
  cin.tie(0), cout.tie(0)
#define ll long long

int main() {
  fast;
  int N, K, tmp;
  vector<int> v;
  cin >> N >> K;
  while (N--) {
    cin >> tmp;
    v.push_back(tmp);
  }
  sort(v.begin(), v.end());
  cout << v[K - 1];
}
