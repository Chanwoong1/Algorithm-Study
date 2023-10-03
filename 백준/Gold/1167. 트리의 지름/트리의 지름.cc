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

vector<pair<int, int> > graph[100001];
int N, v, node, dist, maxV = 0, maxDist = 0;
bool visited[100001];

void dfs(int curr, int d) {
  if (d > maxDist) maxDist = d, maxV = curr;
  visited[curr] = true;
  for (pair<int, int> next : graph[curr]) {
    if (!visited[next.first]) {
      dfs(next.first, d + next.second);
    }
  }
}

int main() {
  fast;
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> v;
    while (1) {
      cin >> node;
      if (node == -1) break;
      cin >> dist;
      graph[v].push_back(make_pair(node, dist));
    }
  }
  dfs(1, 0);
  memset(visited, false, sizeof(visited));
  dfs(maxV, 0);
  cout << maxDist;
}
