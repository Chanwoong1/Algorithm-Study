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
  int N, M, _i, _j, _b[101];
  memset(_b, 0, sizeof(_b));
  cin >> N >> M;
  for (int i = 1; i <= N; i++) _b[i] = i;
  while (M--) {
    cin >> _i >> _j;
    int tmp = _b[_i];
    _b[_i] = _b[_j];
    _b[_j] = tmp;
  }
  for (int i = 1; i <= N; i++) cout << _b[i] << " ";
}
