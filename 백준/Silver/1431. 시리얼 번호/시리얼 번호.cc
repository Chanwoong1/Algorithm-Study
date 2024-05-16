#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

#define fast                        \
  ios_base::sync_with_stdio(false); \
  cin.tie(0), cout.tie(0)
#define ll long long

class Serial {
 public:
  string serial;

  Serial() {}

  Serial(string serial) { this->serial = serial; }

  bool operator<(const Serial &serial) const {
    if (this->serial.length() < serial.serial.length())
      return true;
    else if (this->serial.length() > serial.serial.length())
      return false;
    else {
      int sum1 = 0, sum2 = 0;
      for (int i = 0; i < this->serial.length(); i++) {
        if (this->serial[i] >= '0' && this->serial[i] <= '9')
          sum1 += this->serial[i] - '0';
        if (serial.serial[i] >= '0' && serial.serial[i] <= '9')
          sum2 += serial.serial[i] - '0';
      }
      if (sum1 < sum2)
        return true;
      else if (sum1 > sum2)
        return false;
      else {
        if (this->serial < serial.serial)
          return true;
        else
          return false;
      }
    }
  }
};

int main() {
  fast;
  int N;
  cin >> N;
  vector<Serial> serials(N);
  for (int i = 0; i < N; i++) {
    string serial;
    cin >> serial;
    serials[i] = Serial(serial);
  }
  sort(serials.begin(), serials.end());
  for (int i = 0; i < N; i++) {
    cout << serials[i].serial << '\n';
  }
}
