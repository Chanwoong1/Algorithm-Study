#include <algorithm>
#include <cmath>
#include <cstring>
#include <deque>
#include <iostream>
#include <vector>

using namespace std;

#define fast                        \
  ios_base::sync_with_stdio(false); \
  cin.tie(0), cout.tie(0)
#define ll long long

// 최솟값 찾기
int main() {
  fast;
  int N, L;
  deque<pair<int, ll> > dq;
  cin >> N >> L;
  ll _numbers[N + 1];
  memset(_numbers, 0, sizeof(_numbers));
  dq.clear();
  for (int i = 0; i < N; i++) cin >> _numbers[i];
  for (int i = 0; i < N; i++) {
    ll tmp = _numbers[i];
    while (dq.size() != 0 && dq.back().second > tmp) dq.pop_back();
    dq.push_back(make_pair(i, tmp));
    if (i - dq.front().first >= L) dq.pop_front();
    cout << dq.front().second << " ";
  }
}
