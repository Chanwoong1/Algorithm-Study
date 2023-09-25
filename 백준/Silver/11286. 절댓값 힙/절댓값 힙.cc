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

int main() {
  fast;
  priority_queue<pair<int, bool>, vector<pair<int, bool> >,
                 greater<pair<int, bool> > >
      pq;
  pair<int, bool> element;
  int N, tmp;
  cin >> N;
  while (N--) {
    cin >> tmp;
    element = make_pair(tmp < 0 ? -1 * tmp : tmp, tmp >= 0);
    if (tmp == 0) {
      if (pq.empty())
        cout << "0\n";
      else {
        cout << (pq.top().second ? pq.top().first : -1 * (pq.top().first))
             << "\n";
        pq.pop();
      }
    } else
      pq.push(element);
  }
}
