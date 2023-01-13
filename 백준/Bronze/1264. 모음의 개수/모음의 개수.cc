#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

int main() {
	std::string s;
	int cnt = 0;
	while (1) {
		std::getline(std::cin, s);
		if (s[0] == '#') break;
		cnt = 0;
		for (int i = 0; i < s.length(); ++i) {
			if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
				++cnt;
			if (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U')
				++cnt;
		}
		std::cout << cnt << std::endl;
	}
}