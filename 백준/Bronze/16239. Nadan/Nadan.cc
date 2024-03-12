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
  int K, N;
  cin >> K >> N;
  vector<int> distribution(N);
  int remaining = K - N;
  for (int i = 0; i < N; ++i) distribution[i] = i + 1, remaining -= i;
  distribution[N - 1] += remaining;
  for (int i = 0; i < N; ++i) cout << distribution[i] << '\n';
}
