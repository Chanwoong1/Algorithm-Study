// Share
// https://www.acmicpc.net/problem/3733

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define fast ios_base::sync_with_stdio(false); cin.tie(0), cout.tie(0)
#define ll long long

int main() {
    int a, b;
    while (scanf("%d %d", &a, &b) == 2) printf("%d\n", b / (a + 1));
}
