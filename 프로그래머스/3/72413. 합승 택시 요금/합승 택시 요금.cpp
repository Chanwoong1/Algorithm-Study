#include <string>
#include <vector>

using namespace std;
const int INF = 1e9;

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
  vector<vector<int>> cost(n + 1, vector<int>(n + 1, INF));
  for (int i = 1; i <= n; ++i) cost[i][i] = 0;
  for (auto& fare : fares) cost[fare[0]][fare[1]] = fare[2], cost[fare[1]][fare[0]] = fare[2];
  for (int k = 1; k <= n; ++k) for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) if (cost[i][k] + cost[k][j] < cost[i][j]) cost[i][j] = cost[i][k] + cost[k][j];

  int minCost = INF;
  for (int i = 1; i <= n; ++i) {
    if (cost[s][i] != INF && cost[i][a] != INF && cost[i][b] != INF) {
      int totalCost = cost[s][i] + cost[i][a] + cost[i][b];
      if (totalCost < minCost) minCost = totalCost;
    }
  }

  return minCost;
}