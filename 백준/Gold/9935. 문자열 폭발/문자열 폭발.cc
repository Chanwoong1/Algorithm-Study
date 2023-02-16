// 문자열 폭발
// https://www.acmicpc.net/problem/9935

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define fast ios_base::sync_with_stdio(false); cin.tie(0), cout.tie(0)
#define ll long long

int main() {
    fast;
    string str, b;
    cin >> str >> b;
    int idx = 0, bIdx = b.length() - 1;
    string ans = "";
    for(int i = 0; i < str.length(); i++){
        ans += str[i];
        if (ans[ans.length() - 1] == b[bIdx]) {
            if(ans.length() >= b.length()){
                int cnt = 1;
                for (int j = bIdx-1; j >= 0; j--)
                    if (ans[ans.length()- (bIdx - j) - 1] == b[j]) cnt++;
                if (b.length() == cnt)
                    for(int bb = 0; bb < b.length(); bb++)
                        ans.pop_back();
            }
        }
    }
    if (ans.length() == 0) cout << "FRULA";
    else cout << ans;
}
