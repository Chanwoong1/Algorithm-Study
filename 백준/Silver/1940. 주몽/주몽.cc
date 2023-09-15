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

// 주몽
int main()
{
    fast;
    int N, M, tmp;
    vector<int> materials;
    materials.clear();
    cin >> N >> M;
    while (N-- && (cin >> tmp))
        materials.push_back(tmp);
    sort(materials.begin(), materials.end());
    int _answer = 0, _start = 0, _end = materials.size() - 1;
    while (_start < _end)
    {
        tmp = materials[_start] + materials[_end];
        if (tmp >= M)
        {
            tmp == M ? _answer++ : _answer;
            _end--;
        }
        else
            _start++;
    }
    cout
        << _answer;
}
