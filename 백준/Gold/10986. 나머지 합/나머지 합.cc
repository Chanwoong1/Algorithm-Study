#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define fast                          \
    ios_base::sync_with_stdio(false); \
    cin.tie(0), cout.tie(0)
#define ll long long

// 나머지 합
int main()
{
    fast;
    ll N, M, arr[1000001], counter[1001], answer = 0;
    memset(arr, 0, sizeof(arr));
    memset(counter, 0, sizeof(counter));
    cin >> N >> M >> arr[0];
    arr[0] %= M;
    counter[arr[0]] += 1;
    for (int i = 1; i < N; i++)
    {
        cin >> arr[i];
        arr[i] = (arr[i] + arr[i - 1]) % M;
        counter[arr[i]] += 1;
    }
    for (int i = 0; i < M; i++)
        answer += (counter[i] * (counter[i] - 1)) / 2;
    cout << answer + counter[0];
}
