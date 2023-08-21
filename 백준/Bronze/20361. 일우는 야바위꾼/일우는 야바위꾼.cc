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
    int n, x, k;
    cin >> n >> x >> k;
    while (k--)
    {
        int a, b;
        cin >> a >> b;
        if (a == x)
            x = b;
        else if (b == x)
            x = a;
    }
    cout << x;
}
