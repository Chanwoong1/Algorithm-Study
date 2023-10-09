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

int N, s, e;
vector<pair<int, int> > times;

int main() {
  fast;
  cin >> N;
  while (N--) cin >> s >> e, times.push_back(make_pair(e, s));
  sort(times.begin(), times.end());
  s = times[0].second, e = times[0].first, N = 1;
  for (int i = 1; i < times.size(); i++)
    if (times[i].second >= e) s = times[i].second, e = times[i].first, N += 1;
  cout << N;
}
