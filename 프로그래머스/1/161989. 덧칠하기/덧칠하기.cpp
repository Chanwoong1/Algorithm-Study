#include <queue>
#include <string>
#include <vector>

using namespace std;

int solution(int n, int m, vector<int> section) {
  int answer = 0;
  queue<int> q;
  for (int i = 0; i < section.size(); i++) q.push(section[i]);
  while (!q.empty()) {
    int front = q.front();
    q.pop();
    while (!q.empty() && q.front() < front + m) q.pop();
    answer++;
  }
  return answer;
}