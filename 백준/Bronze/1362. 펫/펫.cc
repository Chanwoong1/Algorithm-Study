#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int main () {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    float o, w, n;
    char ef;
    int cnt = 1;
    int die = 0;
    while (1) {
        scanf("%f %f", &o, &w);
        die = 0;
        if (o == 0 && w == 0)
            break;
        while (1) {
            scanf("%s %f", &ef, &n);
            if (ef == '#')
                break;
            else if (ef == 'F')
                w += n;
            else
                w -= n;
            // printf("%f, %f, %d\n", w, n, die);
            if (w <= 0)
                die = 1;
        }
        if (die)
            printf("%d RIP\n", cnt);
        else if (w > o / 2 && w < o * 2)
            printf("%d :-)\n", cnt);
        else
            printf("%d :-(\n", cnt);
        cnt++;
    }
    return 0;
}