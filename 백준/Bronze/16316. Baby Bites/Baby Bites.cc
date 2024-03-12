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
  int N;
  cin >> N;
  bool b = true;
  for (int i = 1; i <= N; i++) {
    string s;
    cin >> s;
    if (!b) continue;
    if (s != "mumble") {
      int number = stoi(s);
      if (number != i) b = false;
    }
  }
  cout << (b ? "makes sense" : "something is fishy") << endl;
}
