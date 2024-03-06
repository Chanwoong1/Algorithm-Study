#include <iostream>

using namespace std;

int main() {
    int N, t = 3, a = 0;
    cin >> N;
    while (t--) {
        int x;
        for (int i = 0; i < N; i++) {
            cin >> x;
            if (x == 7) a++;
        }
    }
    cout << (a == 3 ? "777" : "0");
}