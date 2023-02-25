#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int k, vector<int> score) {
    vector<int> answer;
    vector<int> q;
    for (int i = 0; i < score.size(); i++) {
        q.push_back(score[i]);
        sort(q.rbegin(), q.rend());
        if (q.size() < k) answer.push_back(q[q.size() - 1]);
        else answer.push_back(q[k - 1]);
    }
    return answer;
}