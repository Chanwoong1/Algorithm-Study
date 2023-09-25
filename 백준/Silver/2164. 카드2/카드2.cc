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

int main() {
  fast;
  int N;
  bool odd = true;
  cin >> N;
  deque<int> dq;
  for (int i = 1; i <= N; i++) dq.push_back(i);
  while (dq.size() != 1) {
    if (odd)
      dq.pop_front();
    else {
      dq.push_back(dq.front());
      dq.pop_front();
    }
    odd = !odd;
  }
  cout << dq.front();
}
