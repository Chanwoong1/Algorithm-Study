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
  string s1, s2, s3, s4, s5;
  cin >> s1 >> s2 >> s3 >> s4 >> s5;
  for (int i = 0; i < 15; i++) {
    if (s1.size() > i) cout << s1[i];
    if (s2.size() > i) cout << s2[i];
    if (s3.size() > i) cout << s3[i];
    if (s4.size() > i) cout << s4[i];
    if (s5.size() > i) cout << s5[i];
  }
}
