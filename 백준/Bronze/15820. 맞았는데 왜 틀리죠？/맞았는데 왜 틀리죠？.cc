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
    int sample = 0, system = 0;
    for (int i = 0; i < n; i++)
    {
        int x, y;
        cin >> x >> y;
        if (x == y)
            sample++;
    }
    for (int i = 0; i < m; i++)
    {
        int x, y;
        cin >> x >> y;
        if (x == y)
            system++;
    }
    if (sample == n && system == m)
        cout << "Accepted";
    else if (sample == n && system != m)
        cout << "Why Wrong!!!";
    else
        cout << "Wrong Answer";
}
