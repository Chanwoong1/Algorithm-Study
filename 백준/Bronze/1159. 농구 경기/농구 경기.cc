#include <iostream>
#include <cstring>
int main() {
	int N;
	int f[26];
	std::memset(f, 0, sizeof(int) * 26);
	std::cin >> N;
	std::string name;
	for (int i = 0; i < N; ++i) {
		std::cin >> name;
		++f[name[0] - 97];
	}
	int ans = 0;
	for (int i = 0; i < 26; ++i) {
		if (f[i] >= 5) {
			std::cout << static_cast<char>(i + 97);
			++ans;
		}
	}
	if (ans == 0)
		std::cout << "PREDAJA\n";
	else
		std::cout << "\n";
}
