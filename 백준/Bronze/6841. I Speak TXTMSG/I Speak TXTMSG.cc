#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <unordered_map>

using namespace std;

#define fast ios_base::sync_with_stdio(false); cin.tie(0), cout.tie(0)
#define ll long long

unordered_map<string, string> short_map;

void madeTable()
{
    short_map["CU"] = "see you";
    short_map[":-)"] = "I’m happy";
    short_map[":-("] = "I’m unhappy";
    short_map[";-)"] = "wink";
    short_map[":-P"] = "stick out my tongue";
    short_map["(~.~)"] = "sleepy";
    short_map["TA"] = "totally awesome";
    short_map["CCC"] = "Canadian Computing Competition";
    short_map["CUZ"] = "because";
    short_map["TY"] = "thank-you";
    short_map["YW"] = "you’re welcome";
    short_map["TTYL"] = "talk to you later";
}

int main()
{
    madeTable();

    string s;
    while (1) {
        cin >> s;
        if (short_map.find(s) == short_map.end()) cout << s << "\n";
        else cout << short_map[s] << "\n";
        
        if (s == "TTYL") break;
    }

    return 0;
}