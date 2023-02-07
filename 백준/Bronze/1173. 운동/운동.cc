#include <iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int N, m, M, T, R;
	cin >> N >> m >> M >> T >> R;
	if (M - m < T)
		cout << "-1\n";
	else {
		int turn;
		int w;
		int x = m;
		for (turn = 0, w = 0; w < N; ++turn) {
			if (x + T <= M) {
				x += T;
				++w;
			}
			else
				x = max(x - R, m);
		}
		cout << turn << "\n";
	}
}
