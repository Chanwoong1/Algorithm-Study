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
  int N, L, answer = 0, i = 0;
  double current = 0;
  cin >> N >> L;
  vector<double> v(N);
  for (int i = 0; i < N; i++) cin >> v[i];
  sort(v.begin(), v.end());
  while (i < N) {
    answer++;
    current = v[i] + L - 1 + 0.5;
    while (i < N && v[i] <= current) i++;
  }
  cout << answer << '\n';
}
