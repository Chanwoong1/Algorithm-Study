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
  string N;
  int B, ans = 0;
  cin >> N >> B;
  for (int i = 0; i < 26; ++i) alpha['A' + i] = i + 10;
  for (int i = 0; i < 10; ++i) alpha['0' + i] = i;
  for (int i = 0; i < N.size(); ++i)
    ans += alpha[N[N.size() - i - 1]] * pow(B, i);
  cout << ans << endl;
}
