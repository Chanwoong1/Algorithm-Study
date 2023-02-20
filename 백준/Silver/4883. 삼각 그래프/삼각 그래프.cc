// 삼각 그래프
// https://www.acmicpc.net/problem/4883

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define fast ios_base::sync_with_stdio(false); cin.tie(0), cout.tie(0)
#define ll long long

#define N 100000
int g[N + 1][3];

int main() {
	int n, k;

	k = 0;
	while (1) {
		k++;
		scanf("%d", &n);
		if (n == 0) break;
		for (int i = 0; i < n; i++) {
			scanf("%d %d %d", &g[i][0], &g[i][1], &g[i][2]);
		}
		g[0][0] = 987654321;
		g[0][2] += g[0][1];
		for (int i = 1; i < n; i++) {
			// 왼쪽
			g[i][0] += min(g[i - 1][0], g[i - 1][1]);
			// 중간
			g[i][1] += min(g[i - 1][0], min(g[i - 1][1], min(g[i - 1][2], g[i][0])));
			// 오른쪽
			g[i][2] += min(g[i - 1][1], min(g[i - 1][2], g[i][1]));
		}
		printf("%d. %d\n", k, g[n - 1][1]);
	}
}
