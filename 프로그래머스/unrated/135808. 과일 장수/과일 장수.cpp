#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, int m, vector<int> score) {
    int answer = 0;
    sort(score.rbegin(), score.rend());
    for (int i = m; i < score.size() + 1; i += m)
        answer += score[i - 1] * m;
    return answer;
}