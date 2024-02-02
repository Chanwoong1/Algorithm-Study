#include <string>
#include <vector>

using namespace std;

void dfs(int n, vector<vector<int>> computers, vector<int>& visited, int start) {
  visited[start] = 1;
  for (int i = 0; i < n; i++) if (computers[start][i] && !visited[i]) dfs(n, computers, visited, i);
}

int solution(int n, vector<vector<int>> computers) {
  int answer = 0;
  vector<int> visited(n, 0);
  for (int i = 0; i < computers.size(); i++) if (!visited[i]) dfs(n, computers, visited, i), answer++;
  return answer;
}