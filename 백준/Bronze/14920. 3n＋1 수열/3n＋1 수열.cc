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
    while (N != 1)
    {
        if (N % 2 == 0)
            N /= 2;
        else
            N = 3 * N + 1;
        answer++;
    }
    cout << answer + 1;
}
