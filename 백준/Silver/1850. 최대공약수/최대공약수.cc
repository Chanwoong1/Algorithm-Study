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

ll A, B;

ll euclid(ll small, ll big) {
  return (big % small == 0 ? small : euclid(big % small, small));
}

int main() {
  fast;
  cin >> A >> B;
  for (ll i = 0; i < euclid(A, B); i++) cout << "1";
}
