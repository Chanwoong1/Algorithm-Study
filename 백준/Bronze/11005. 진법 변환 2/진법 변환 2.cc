#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

#define fast                        \
  ios_base::sync_with_stdio(false); \
  cin.tie(0), cout.tie(0)
#define ll long long

int main() {
  fast;
  map<char, int> alpha;
  string ans = "";
  int N, B;
  cin >> N >> B;
  for (int i = 0; i < 26; ++i) alpha['A' + i] = i + 10;
  for (int i = 0; i < 10; ++i) alpha['0' + i] = i;
  while (N) {
    int tmp = N % B;
    if (tmp >= 10)
      ans += 'A' + tmp - 10;
    else
      ans += '0' + tmp;
    N /= B;
  }
  reverse(ans.begin(), ans.end());
  cout << ans << endl;
}
