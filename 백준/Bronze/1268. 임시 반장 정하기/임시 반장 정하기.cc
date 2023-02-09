#include <iostream>
#include <cstring>
#include <set>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0), cout.tie(0);
	int N;
	cin >> N;
	int student[N][6];
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < 5; ++j) {
			cin >> student[i][j];
		}
	}
	set<int> answer[N];
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < 5; ++j) {
			for (int k = 0; k < N; ++k) {
				if (student[i][j] == student[k][j] && i != k)
					answer[i].insert(k);
			}
		}
	}
	int ans = 0;
	int max = 0;
	for (int i = 0; i < N; ++i) {
		if (answer[i].size() > max) {
			ans = i;
			max = answer[i].size();
		}
	}
	cout << ans + 1 << "\n";
}
