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
    int n;
    cin >> n;
    int answer = 0;
    while (n--)
    {
        int x;
        cin >> x;
        answer = max(answer, x);
    }
    cout << answer;
}
