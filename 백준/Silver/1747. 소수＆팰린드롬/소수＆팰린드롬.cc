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

int N;
bool er[1100001];  // 소수 판별을 위한 배열. 소수가 아니면 true, 소수이면 false.

bool isPalindrome(int i) {
  string ii = to_string(i);
  for (int idx = 0; idx < ii.length() / 2; idx++) {
    if (ii[idx] != ii[ii.length() - idx - 1]) return false;
  }
  return true;
}

void eratos() {  // 에라토스테네스의 체 구현
  for (int i = 2; i <= 1100001; i++) er[i] = true;
  for (int i = 2; i * i <= 1100001; i++)
    if (er[i])
      for (int k = i * i; k <= 1100001; k += i) er[k] = false;
}

int main() {
  fast;
  cin >> N;
  eratos();
  while (!er[N] || !isPalindrome(N)) N++;
  cout << N;
}
