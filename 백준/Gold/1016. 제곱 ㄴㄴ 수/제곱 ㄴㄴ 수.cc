#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

#define fast                        \
  ios_base::sync_with_stdio(false); \
  cin.tie(0), cout.tie(0)
#define ll long long

ll _min, _max, idx, tmp;

int main() {
  fast;
  cin >> _min >> _max;
  vector<ll> answer(_max - _min + 1, 1);
  idx = 2;
  while (idx * idx <= _max) {
    tmp = _min / (idx * idx);
    while (tmp * idx * idx <= _max) {
      if (tmp * idx * idx >= _min) answer[tmp * idx * idx - _min] = 0;
      tmp++;
    }
    idx++;
  }
  cout << accumulate(answer.begin(), answer.end(), 0);
}
