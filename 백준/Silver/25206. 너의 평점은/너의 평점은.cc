#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

#define fast                        \
  ios_base::sync_with_stdio(false); \
  cin.tie(0), cout.tie(0)
#define ll long long

int main() {
  fast;
  int N = 20;
  float _sum1 = 0, _sum2 = 0, _s;
  string tmp, sub, grade;
  while (N--) {
    getline(cin, tmp);
    if (tmp[tmp.size() - 1] == '\n') tmp.replace(tmp.size() - 1, 1, "");
    istringstream sp(tmp);
    sp >> sub >> _s >> grade;
    if (grade == "A+")
      _sum1 += _s * 4.5;
    else if (grade == "A0")
      _sum1 += _s * 4;
    else if (grade == "B+")
      _sum1 += _s * 3.5;
    else if (grade == "B0")
      _sum1 += _s * 3;
    else if (grade == "C+")
      _sum1 += _s * 2.5;
    else if (grade == "C0")
      _sum1 += _s * 2;
    else if (grade == "D+")
      _sum1 += _s * 1.5;
    else if (grade == "D0")
      _sum1 += _s * 1;

    if (grade != "P") _sum2 += _s;
  }
  cout << _sum1 / _sum2;
}
