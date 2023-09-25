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
  int N, tmp, answer = 0;
  vector<int> v;
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> tmp;
    v.push_back(tmp);
  }
  sort(v.begin(), v.end());
  for (int i = 1; i < N; i++) v[i] += v[i - 1];
  for (int i = 0; i < N; i++) answer += v[i];
  cout << answer;
}
