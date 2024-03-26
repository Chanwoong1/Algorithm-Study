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
  int N, group = 1;
  while (1) {
    cin >> N;
    if (N == 0) break;
    vector<pair<string, vector<string>>> v;
    for (int i = 0; i < N; i++) {
      string s;
      cin >> s;
      vector<string> v2;
      for (int j = 0; j < N - 1; j++) {
        string s2;
        cin >> s2;
        v2.push_back(s2);
      }
      v.push_back({s, v2});
    }
    cout << "Group " << group << "\n";
    int count = 0;
    for (int i = 0; i < v.size(); i++) {
      string name = v[i].first;
      for (int j = 0; j < v[i].second.size(); j++) {
        string np = v[i].second[j];
        if (np == "N") {
          count++;
          int index = (i - j + N - 1) % N;
          cout << v[index].first << " was nasty about " << name << "\n";
        }
      }
    }
    if (count == 0) cout << "Nobody was nasty\n";
    cout << "\n";
    group++;
  }
}
