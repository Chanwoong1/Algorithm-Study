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
    while(1) {
        cin >> a;
        if (a == 0) break;
        printf("%.2f\n", 1 + a + pow(a,2) + pow(a,3) + pow(a,4));
    }
}