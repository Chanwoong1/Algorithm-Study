#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int N, Q;
int Song[101];

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> Q;
    int s;
    Song[0] = 0;
    for (int i = 1; i <= N; ++i) {
        cin >> s;
        Song[i] = Song[i - 1] + s;
    }
    int q;
    for (int i = 0; i < Q; ++i) {
        cin >> q;
        for (int j = 0; j < N; ++j) {
            if (Song[j] <= q && Song[j + 1] > q)
                cout << j + 1 << "\n";
        }
    }
    return 0;
}
