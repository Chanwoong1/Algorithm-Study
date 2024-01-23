#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm> // sort 함수 사용을 위해 포함

using namespace std;

bool compare(pair<int, int> &a, pair<int, int> &b) { return a.second > b.second; }

int solution(int k, vector<int> tangerine) {
    map<int, int> t;
    for (auto tt : tangerine) t[tt]++;
    vector<pair<int, int>> vec(t.begin(), t.end());
    sort(vec.begin(), vec.end(), compare);
    int answer = 0;
    for (int i = 0; i < vec.size(); i++) {
        k -= vec[i].second;
        answer++;
        if (k <= 0) break;
    }
    return answer;
}