#include <string>
#include <vector>

using namespace std;

string solution(vector<string> survey, vector<int> choices) {
    string answer = "";
    int rt = 0, cf = 0, jm = 0, an = 0;
    for (int i = 0; i < survey.size(); i++) {
        if (survey[i] == "AN") an += choices[i] - 4;
        else if (survey[i] == "NA") an -= (choices[i] - 4);
        else if (survey[i] == "RT") rt += (choices[i] - 4);
        else if (survey[i] == "TR") rt -= (choices[i] - 4);
        else if (survey[i] == "CF") cf += (choices[i] - 4);
        else if (survey[i] == "FC") cf -= (choices[i] - 4);
        else if (survey[i] == "JM") jm += (choices[i] - 4);
        else if (survey[i] == "MJ") jm -= (choices[i] - 4);
    }
    (rt > 0) ? answer += "T" : answer += "R";
    (cf > 0) ? answer += "F" : answer += "C";
    (jm > 0) ? answer += "M" : answer += "J";
    (an > 0) ? answer += "N" : answer += "A";
    return answer;
}