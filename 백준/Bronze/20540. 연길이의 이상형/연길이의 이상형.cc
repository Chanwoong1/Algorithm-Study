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
    string mbti;
    cin >> mbti;
    string answer = "";
    for (int i = 0; i < 4; i++)
    {
        if (mbti[i] == 'E')
            answer += 'I';
        else if (mbti[i] == 'I')
            answer += 'E';
        else if (mbti[i] == 'S')
            answer += 'N';
        else if (mbti[i] == 'N')
            answer += 'S';
        else if (mbti[i] == 'T')
            answer += 'F';
        else if (mbti[i] == 'F')
            answer += 'T';
        else if (mbti[i] == 'J')
            answer += 'P';
        else if (mbti[i] == 'P')
            answer += 'J';
    }
    cout << answer;
}
