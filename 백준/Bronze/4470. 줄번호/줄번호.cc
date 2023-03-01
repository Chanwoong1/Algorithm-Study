// 줄 번호
// https://www.acmicpc.net/problem/4470

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
    string N, s;
    getline(cin, N);
    for (int i = 1; i <= stoi(N); i++) {
        getline(cin, s);
        cout << i << ". " << s << "\n";
    }
}
