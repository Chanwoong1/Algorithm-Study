#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    string s;
    vector<int> alpha;
    for (int i = 0; i < 26; ++i)
        alpha.push_back(0);
    while (1) {
        cin >> s;
        if (cin.eof())
            break;
        for (int i = 0; i < s.length(); ++i) {
            ++alpha[s[i] - 97];
        }
    }
    int max = *max_element(alpha.begin(), alpha.end());
    for (int i = 0; i < 26; ++i) {
        if (alpha[i] == max)
            cout << (char)('a' + i);
    }
    return 0;
}
