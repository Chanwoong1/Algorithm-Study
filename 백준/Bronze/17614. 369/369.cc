#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define fast                          \
    ios_base::sync_with_stdio(false); \
    cin.tie(0), cout.tie(0)
#define ll long long

int main()
{
    fast;
    int N;
    cin >> N;
    int answer = 0;
    for (int i = 1; i <= N; i++)
    {
        string s = to_string(i);
        for (int j = 0; j < s.size(); j++)
        {
            if (s[j] == '3' || s[j] == '6' || s[j] == '9')
            {
                answer++;
                break;
            }
        }
    }
    cout << answer;
}
