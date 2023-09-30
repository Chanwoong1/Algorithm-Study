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

bool visited[1001];
vector<int> graph[1001];

void dfs(int curr) {
  visited[curr] = true;
  for (int i = 0; i < graph[curr].size(); i++) {
    int next = graph[curr][i];
    if (!visited[next]) dfs(next);
  }
}

int main() {
  fast;
  int N, M, x, y, answer = 0;
  cin >> N >> M;
  for (int i = 0; i < M; i++) {
    cin >> x >> y;
    graph[x].push_back(y);
    graph[y].push_back(x);
  }
  for (int i = 1; i <= N; i++) {
    if (!visited[i]) {
      answer++;
      dfs(i);
    }
  }
  cout << answer;
}
