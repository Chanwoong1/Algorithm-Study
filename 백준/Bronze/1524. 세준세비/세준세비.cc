// 세준세비
// https://www.acmicpc.net/problem/1524

#include<cstdio>
#define max(x, y) x > y ? x : y;
int T;
int main() {
    for (scanf("%d", &T); T--;) {
        int n, m, x, p = 0, q = 0;
        scanf("%d%d", &n, &m);
        while (n--) scanf("%d", &x), p = max(x, p);
        while (m--) scanf("%d", &x), q = max(x, q);
        puts(p < q ? "B" : "S");
    }
    return 0;
}