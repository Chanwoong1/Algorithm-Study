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

int N, K, ans, coins[10];

int main() {
  fast;
  cin >> N >> K;
  for (int i = 0; i < N; i++) cin >> coins[i];
  for (int i = N - 1; i >= 0; i--) ans += K / coins[i], K %= coins[i];
  cout << ans;
}
