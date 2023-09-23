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
  int N, tmp, idx;
  stack<int> st;
  cin >> N;
  int answer[N], lst[N];
  memset(lst, 0, sizeof(lst));
  for (int i = 0; i < N; i++) answer[i] = -1;
  for (int i = 0; i < N; i++) cin >> lst[i];
  st.push(0);
  for (int i = 1; i < N; i++) {
    while (!st.empty() && lst[st.top()] < lst[i]) {
      answer[st.top()] = lst[i];
      st.pop();
    }
    st.push(i);
  }
  for (int i = 0; i < N; i++) cout << answer[i] << " ";
}