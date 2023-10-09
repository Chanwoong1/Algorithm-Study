#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define fast                        \
  ios_base::sync_with_stdio(false); \
  cin.tie(0), cout.tie(0)
#define ll long long

int N, tmp, ans, v;
priority_queue<int, vector<int>, greater<int> > pq;

int main() {
  fast;
  cin >> N;
  while (N--) cin >> tmp, pq.push(tmp);
  while (pq.size() != 1)
    v = pq.top(), pq.pop(), v += pq.top(), pq.pop(), ans += v, pq.push(v);
  cout << ans;
}
