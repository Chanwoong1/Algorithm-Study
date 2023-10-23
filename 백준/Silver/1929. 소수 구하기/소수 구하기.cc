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

int N, M;
bool er[1000001];

void eratos() {
  er[0] = true, er[1] = true;
  for (int i = 2; i * i <= 1000001; i++)
    if (!er[i])
      for (int k = i * i; k <= 1000001; k += i) er[k] = true;
}

int main() {
  fast;
  cin >> M >> N;
  eratos();
  for (int i = M; i <= N; i++)
    if (!er[i]) cout << i << "\n";
}
