#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

#define fast                        \
  ios_base::sync_with_stdio(false); \
  cin.tie(0), cout.tie(0)
#define ll long long

int main() {
  fast;
  int n, m, i = 1;
  stack<int> st;
  bool ans = true;
  string answer = "";
  cin >> n;
  while (n--) {
    cin >> m;
    int topOfStack = st.empty() == true ? 0 : st.top();
    if (topOfStack < m) {
      while (i <= m) {
        st.push(i);
        answer += "+\n";
        if (i == m) {
          st.pop();
          answer += "-\n";
        }
        i++;
      }
    } else if (topOfStack == m) {
      st.pop();
      answer += "-\n";
    } else
      ans = false;
  }
  ans ? cout << answer : cout << "NO";
}
