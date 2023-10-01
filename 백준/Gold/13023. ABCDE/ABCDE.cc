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

bool visited[2001], answer;
vector<int> friends[2001];

void dfs(pair<int, int> curr) {
  if (curr.second == 5) {
    answer = true;
    return;
  }
  for (int next : friends[curr.first]) {
    if (!visited[next]) {
      visited[next] = true;
      dfs(make_pair(next, curr.second + 1));
      visited[next] = false;
    }
  }
}

int main() {
  fast;
  int N, M, a, b;
  cin >> N >> M;
  while (M--) cin >> a >> b, friends[a].push_back(b), friends[b].push_back(a);
  for (int i = 0; i < N; i++) {
    memset(visited, false, sizeof(visited));
    visited[i] = true, dfs(make_pair(i, 1));
    if (answer) break;
  }
  cout << (answer ? "1" : "0");
}
