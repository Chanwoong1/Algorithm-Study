// 치킨 쿠폰
// https://www.acmicpc.net/problem/1673

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int n, k;

int main() {
    while (scanf("%d %d", &n, &k) != -1) {
        int ans = 0, c = n, tmp = 0;
        while (c) {
            ans += c;
            tmp += c;
            c = tmp / k;
            tmp %= k;
        }
        printf("%d\n", ans);
    }
    return 0;
}
