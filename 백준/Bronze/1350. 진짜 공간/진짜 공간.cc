#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int main () {
    vector<int> files;
    int N, cluster;
    scanf("%d", &N);
    long long file;
    for (int i = 0; i < N; ++i) {
        scanf("%lld", &file);
        files.push_back(file);
    }
    scanf("%d", &cluster);
    long long answer = 0;
    for (int i = 0; i < files.size(); ++i) {
        if (files[i] == 0)
            continue;
        answer += files[i] / cluster;
        if (files[i] % cluster != 0)
            ++answer;
    }
    printf("%lld", answer * cluster);
    return 0;
}
