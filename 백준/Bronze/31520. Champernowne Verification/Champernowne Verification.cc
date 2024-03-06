#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    string s;
    int a = 1;
    cin >> s;
    for (int i = 0; i < s.length(); i++) {
        if (s.substr(i, to_string(a).length()) != to_string(a)) {a = 0; break;}
        a++;
    }
    cout << a - 1;
}