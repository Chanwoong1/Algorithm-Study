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

int main()
{
    fast;
    int C, K, P;
    cin >> C >> K >> P;
    int answer = 0;
    for (int i = 1; i <= C; i++)
    {
        answer += K * i + P * i * i;
    }
    cout << answer;
}
