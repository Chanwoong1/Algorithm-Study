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

#define MAX 100000001
int nextValues[4] = {1, 3, 7, 9};

bool isPrime(int num) {
  for (int i = 2; i * i <= num; i++)
    if (num % i == 0) return false;
  return true;
}

void dfs(pair<int, int> curr, int depth) {
  if (curr.second == depth) {
    cout << curr.first << "\n";
    return;
  }
  for (int next : nextValues) {
    int nextValue = curr.first * 10 + next;
    if (isPrime(nextValue)) {
      dfs(make_pair(nextValue, curr.second + 1), depth);
    }
  }
}

int main() {
  fast;
  int N, starts[4] = {2, 3, 5, 7};
  cin >> N;
  for (int next : starts) {
    dfs(make_pair(next, 1), N);
  }
}
