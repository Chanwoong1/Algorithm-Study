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

int N, M, tmp, sum = 0, s = 0, e = 0;
vector<int> v;

int main() {
  fast;
  cin >> N >> M;
  while (N--) cin >> tmp, s = max(s, tmp), e += tmp, v.push_back(tmp);
  while (s <= e) {
    int mid = (s + e) / 2, cnt = 0, sum = 0;
    for (int i = 0; i < v.size(); i++) {
      if (sum + v[i] > mid) cnt++, sum = 0;
      sum += v[i];
    }
    if (sum != 0) cnt++;
    if (M >= cnt)
      e = mid - 1;
    else if (M < cnt)
      s = mid + 1;
  }
  cout << s;
}
