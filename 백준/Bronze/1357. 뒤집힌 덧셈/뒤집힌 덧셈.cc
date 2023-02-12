#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int rev(string s) {
    string ret;

    ret = "";
    for (int i = s.length() - 1; i > -1; --i)
        ret += s[i];
    return stoi(ret);
}

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    string X, Y;
    cin >> X >> Y;
    cout << rev(to_string(rev(X) + rev(Y)));
}
