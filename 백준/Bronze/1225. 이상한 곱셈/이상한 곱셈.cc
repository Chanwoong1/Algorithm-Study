#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	std::string a, b;
	cin >> a >> b;
	long long answer = 0;
	for (int i = 0; i < a.size(); ++i) {
		for (int j = 0; j < b.size(); ++j) {
			answer += (static_cast<int>(a[i]) - 48) * (static_cast<int>(b[j]) - 48);
		}
	}
	cout << answer << "\n";
}