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
  int nums[10], N;
  memset(nums, 0, sizeof(nums));
  cin >> N;
  while (N >= 10) {
    nums[N % 10]++;
    N /= 10;
  }
  nums[N]++;
  for (int i = 9; i >= 0; i--)
    while (nums[i]-- > 0) cout << i;
}
