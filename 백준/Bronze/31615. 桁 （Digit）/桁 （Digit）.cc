#include <iostream>
#include <string>
using namespace std;
int main() {
    int A, B;
    cin >> A >> B;
    string s = to_string(A + B);
    cout << s.length();
}