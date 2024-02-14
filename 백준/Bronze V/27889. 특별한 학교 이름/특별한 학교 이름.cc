#include <iostream>

using namespace std;

int main() {
    string s;
    cin >> s;
    cout << (s == "NLCS" ? "North London Collegiate School" : s == "BHA" ? "Branksome Hall Asia" : s == "KIS" ? "Korea International School" : "St. Johnsbury Academy");
}
