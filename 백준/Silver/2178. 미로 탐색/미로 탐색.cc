// 미로 탐색
// https://www.acmicpc.net/problem/2178

#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define fast ios_base::sync_with_stdio(false); cin.tie(0), cout.tie(0)
#define ll long long

int visited[101][101];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
string map[101];
int N, M;

void dfs(int x, int y) {
    if (x == N - 1 && y == M - 1)
        return ;
    for (int i = 0; i < 4; ++i) {
        int nX = x + dx[i], nY = y + dy[i];
        if (nX >= 0 && nX < N && nY >= 0 && nY < M) {
            if ((visited[nX][nY] == 0 && map[nX][nY] == '1') || (map[nX][nY] == '1' && visited[nX][nY] > visited[x][y] + 1)) {
                visited[nX][nY] = visited[x][y] + 1;
                dfs(nX, nY);
            }
        }
    }
}

int main() {
    fast;
    cin >> N >> M;
    for (int i = 0; i < N; ++i) cin >> map[i];
    for (int i = 0; i < 101; ++i) {
        memset(visited[i], 0, sizeof(int) * 101);
    }
    visited[0][0] = 1;
    dfs(0, 0);
    cout << visited[N - 1][M - 1];
}
