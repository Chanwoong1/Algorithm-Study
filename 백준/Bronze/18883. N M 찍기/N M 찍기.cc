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
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n * m; i++)
    {
        cout << i;
        if (i % m == 0)
            cout << '\n';
        else
            cout << ' ';
    }
}
