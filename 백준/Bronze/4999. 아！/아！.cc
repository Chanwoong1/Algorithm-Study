#include <iostream>
#include <string>

int main() {
	std::string jw;
	std::string doc;

	std::cin >> jw;
	std::cin >> doc;
	(jw.length() < doc.length()) ? std::cout << "no\n" : std::cout << "go\n";
	return 0;
}