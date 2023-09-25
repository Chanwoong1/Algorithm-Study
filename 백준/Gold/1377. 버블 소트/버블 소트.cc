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
  int N, tmp;
  vector<pair<int, int> > v;
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> tmp;
    v.push_back(make_pair(tmp, i));
  }
  sort(v.begin(), v.end());
  int answer = 0;
  for (int i = 0; i < N; i++) answer = max(answer, v[i].second - i);
  cout << answer + 1;
}
