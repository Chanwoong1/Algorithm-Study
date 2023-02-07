#include <iostream>
#include <cstring>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0), cout.tie(0);

	int N, M;
	cin >> N >> M;
	char castle[N][M + 1];
	int ans = 0;
	int add;
	for (int i = 0; i < N; ++i) {
		cin >> castle[i];
		add = 1;
		for (int j = 0; j < M; ++j) {
			if (castle[i][j] == 'X')
				add = 0;
		}
		if (add == 1)
			++ans;
	}
	int ans2 = 0;
	for (int i = 0; i < M; ++i) {
		add = 1;
		for (int j = 0; j < N; ++j) {
			if (castle[j][i] == 'X')
				add = 0;
		}
		if (add == 1)
			++ans2;
	}
	(ans > ans2) ? cout << ans << "\n" : cout << ans2 << "\n";
}
