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
    int student[N];
    for (int i = 0; i < N; i++)
    {
        cin >> student[i];
        if (student[i] != i + 1)
            answer++;
    }
    cout << answer;
}
