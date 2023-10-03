#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

#define fast                        \
  ios_base::sync_with_stdio(false); \
  cin.tie(0), cout.tie(0)
#define ll long long

bool visited[1001];
int dx[4], dy[4];
vector<int> graph[1001];

void dfs(int curr) {
  cout << curr << " ";
  visited[curr] = true;
  for (int next : graph[curr])
    if (!visited[next]) dfs(next);
}

void bfs(int start) {
  queue<int> q;
  q.push(start), visited[start] = true;

  while (!q.empty()) {
    int curr = q.front();
    q.pop();
    cout << curr << " ";
    for (int next : graph[curr])
      if (!visited[next]) q.push(next), visited[next] = true;
  }
}

int main() {
  fast;
  int N, M, V, x, y;
  dx[0] = 1, dx[1] = -1, dy[2] = 1, dy[3] = -1;
  cin >> N >> M >> V;
  while (M--) cin >> x >> y, graph[x].push_back(y), graph[y].push_back(x);
  for (int i = 0; i <= N; i++) sort(graph[i].begin(), graph[i].end());
  dfs(V);
  cout << "\n";
  memset(visited, false, sizeof(visited));
  bfs(V);
}
