#include <string>
#include <vector>

using namespace std;

int solution(vector<string> babbling)
{
    int answer = 0;
    for (int bb_idx = 0; bb_idx < babbling.size(); ++bb_idx) {
        vector<string> word{ "aya", "ye", "woo", "ma" };
        string prev{ "" };
        for (int w_idx = 0; w_idx < word.size(); ++w_idx) {
            if (prev != word[w_idx] && babbling[bb_idx].substr(0, word[w_idx].length()) == word[w_idx]) {   
                babbling[bb_idx] = babbling[bb_idx].substr(word[w_idx].length(), babbling[bb_idx].length() - 1);
                prev = word[w_idx];
                w_idx = -1;
            }
        }
        if (babbling[bb_idx].empty()) ++answer;
    }
    return answer;
}