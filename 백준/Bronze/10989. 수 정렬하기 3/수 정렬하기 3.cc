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
  int N, tmp, arr[10001];
  memset(arr, 0, sizeof(arr));
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> tmp;
    arr[tmp]++;
  }
  for (int i = 0; i < 10001; i++)
    while (arr[i]-- > 0) cout << i << "\n";
}
