#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

#define fast                        \
  ios_base::sync_with_stdio(false); \
  cin.tie(0), cout.tie(0)
#define ll long long

int main() {
  fast;
  int N, firstCharCount = 0;
  string s;
  cin >> N >> s;
  for (int i = 0; i < N; i++) {
    if (s[i] == s[0]) {
      firstCharCount++;
    }
  }
  cout << (firstCharCount == N ? "Yes" : "No");
}
