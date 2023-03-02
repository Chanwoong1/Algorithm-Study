#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define fast ios_base::sync_with_stdio(false); cin.tie(0), cout.tie(0)
#define ll long long

double a;

int main() {
    while (1) {
        cin >> a;
        if (a == -1) break;
        printf("Objects weighing %.2f on Earth will weigh %.2f on the moon.\n", a, a * 0.167);
    }
}
