// DNA 해독
// https://www.acmicpc.net/problem/1672

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

string DNA = "ACAGCGTAATCGGAGT";

char fn(char a, char b) {
    int idx = (a == 'A' ? 0 : a == 'G' ? 1 : a == 'C' ? 2 : 3);
    int idx2 = (b == 'A' ? 0 : b == 'G' ? 1 : b == 'C' ? 2 : 3);
    return DNA[idx * 4 + idx2];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int N;
    cin >> N;
    string strN;
    cin >> strN;
    for (int i = strN.length() - 2; i > - 1; i--) {
        strN[i] = fn(strN[i], strN[i + 1]);
    }
    cout << strN[0];
    return 0;
}
