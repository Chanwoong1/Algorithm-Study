// 타임머신
// https://www.acmicpc.net/problem/1440

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int solution(vector<string> strs)
{
	int count = 0;
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			for (int k = 0; k < 3; k++)
				if (i != j && j != k && k != i)
					if ((stoi(strs[i]) >= 1 && stoi(strs[i]) <= 12) && stoi(strs[j]) >= 0 && stoi(strs[j]) <= 59 && stoi(strs[k]) >= 0 && stoi(strs[k]) <= 59)
						count++;
	return count;
}

int main () {
    ios::sync_with_stdio(false);
    string t;
    vector<string> time;
    cin >> t;
    time.push_back(t.substr(0, 2));
    time.push_back(t.substr(3, 5));
    time.push_back(t.substr(6, 8));
    cout << solution(time);
}
