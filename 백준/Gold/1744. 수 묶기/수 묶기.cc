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

int N, ans, tmp, p1, p2;
priority_queue<int, vector<int>, greater<int> > pq;

int main() {
  fast;
  cin >> N;
  while (N--) cin >> tmp, pq.push(tmp);
  while (!pq.empty()) {
    p1 = pq.top(), pq.pop();
    if (pq.empty()) {
      ans += p1;
      break;
    } else if (p1 > 0 && pq.size() % 2 == 0) {
      ans += p1;
      continue;
    }
    p2 = pq.top(), pq.pop();
    if (p1 == 0)
      pq.push(p2);
    else if (p2 == 0)
      ;
    else if (p1 == 1)
      ans += 1, pq.push(p2);
    else if (p2 == 1)
      ans += p1 + 1;
    else if (p1 < 0 && p2 > 0)
      ans += p1, pq.push(p2);
    else
      ans += p1 * p2;
  }
  cout << ans;
}
