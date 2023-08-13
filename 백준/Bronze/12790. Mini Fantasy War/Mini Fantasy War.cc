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
    int T;
    cin >> T;
    int hp, mp, atk, def, hp_, mp_, atk_, def_;
    while (T--)
    {
        cin >> hp >> mp >> atk >> def >> hp_ >> mp_ >> atk_ >> def_;
        hp += hp_;
        mp += mp_;
        atk += atk_;
        def += def_;
        if (hp < 1)
            hp = 1;
        if (mp < 1)
            mp = 1;
        if (atk < 0)
            atk = 0;
        cout << hp + 5 * mp + 2 * atk + 2 * def << '\n';
    }
}
