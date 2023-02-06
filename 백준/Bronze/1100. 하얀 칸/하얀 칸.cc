#include <iostream>
int main() {
	char chess[8][9];
	for (int i = 0; i < 8; ++i)
		std::cin >> chess[i];
	int ans = 0;
	for (int i = 0; i < 8; i++) {
		for (int j = i % 2; j < 8; j += 2) {
			if (chess[i][j] == 'F')
				++ans;
		}
	}
	std::cout << ans << "\n";
}
