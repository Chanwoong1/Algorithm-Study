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
    int N, _start = 0, _end = 1, _sum = 1, _answer = 0;
    cin >> N;
    while (_start != _end)
    {
        if (_sum < N)
        {
            _end++;
            _sum += _end;
        }
        else if (_sum == N)
        {
            _answer++;
            _end++;
            _sum += _end;
        }
        else
        {
            _sum -= _start;
            _start++;
        }
    }
    cout << _answer + (N == 1 ? 0 : 1);
}
