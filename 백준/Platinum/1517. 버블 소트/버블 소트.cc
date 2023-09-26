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

vector<ll> arr;
ll ans = 0, sorted[500001];

void merge(int left, int mid, int right) {
  int i = left;
  int j = mid + 1;
  int k = left;
  while (i <= mid && j <= right) {
    if (arr[i] <= arr[j]) {
      sorted[k] = arr[i];
      i++;
    } else {
      sorted[k] = arr[j];
      ans += j - k;
      j++;
    }
    k++;
  }
  if (i > mid) {
    for (int x = j; x <= right; x++) {
      sorted[k] = arr[x];
      k++;
    }
  } else {
    for (int x = i; x <= mid; x++) {
      sorted[k] = arr[x];
      k++;
    }
  }
  for (int x = left; x <= right; x++) {
    arr[x] = sorted[x];
  }
}

void merge_sort(int left, int right) {
  if (left >= right) return;
  int mid = (left + right) >> 1;
  merge_sort(left, mid);
  merge_sort(mid + 1, right);
  merge(left, mid, right);
}

int main(void) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int n, k;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> k;
    arr.push_back(k);
  }
  merge_sort(0, n - 1);
  cout << ans;
  return 0;
}
