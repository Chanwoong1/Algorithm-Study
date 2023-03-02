#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define fast ios_base::sync_with_stdio(false); cin.tie(0), cout.tie(0)
#define ll long long

int main() {
    fast;
    int n;
    cin >> n;
    while (n--) {
        string s;
        cin >> s;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] >= 65 && s[i] <= 90) cout << (char)(s[i] + 32);
            else cout << s[i];
        }
        cout << "\n";
    }
}
