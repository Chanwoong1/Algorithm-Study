#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    string N;
    cin >> N;
    int tmp1, tmp2;
    bool ans = false;
    for (int i = 1; i < N.length(); ++i) {
        tmp1 = 1;
        tmp2 = 1;
        for (int j = 0; j < i; ++j) {
            tmp1 *= (N[j] - '0');
        }
        for (int j = i; j < N.length(); ++j) {
            tmp2 *= (N[j] - '0');
        }
        if (tmp1 == tmp2)
            ans = true;
    }
    if (ans)
        cout << "YES";
    else
        cout << "NO";
    return 0;
}
