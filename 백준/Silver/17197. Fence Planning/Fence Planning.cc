#include <bits/stdc++.h>
using namespace std;

const int INF = 987654321;

vector<int> parent;
vector<tuple<int, int, int, int>> vp;	//max <y, x>, min <y, x>

void init(int sz) {
	parent.resize(sz);
	for (int i = 0; i < sz; ++i)
		parent[i] = i;
}

int find(int u) {
	if (u == parent[u]) return u;
	return parent[u] = find(parent[u]);
}

void merge(int u, int v) {
	u = find(u), v = find(v);
	if (u == v) return;
	parent[u] = v;
}


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	
	int n, m;
	cin >> n >> m;

	init(n);
	vp.resize(n);
	int u, v;
	for (int i = 0; i < n; ++i) {
		cin >> u >> v;
		vp[i] = { v, u, v, u };
	}

	for (int i = 0; i < m; ++i) {
		cin >> u >> v;
		--u, --v;
		u = find(u), v = find(v);

		if (u != v) {
			vp[v] = make_tuple(
				max(get<0>(vp[u]), get<0>(vp[v])),
				max(get<1>(vp[u]), get<1>(vp[v])),
				min(get<2>(vp[u]), get<2>(vp[v])),
				min(get<3>(vp[u]), get<3>(vp[v]))
			);

			merge(u, v);
		}
	}

	int min_perimeter = INF;
	for (int i = 0; i < n; ++i) {
		if (i != find(i)) continue;

		auto& [max_y, max_x, min_y, min_x] = vp[i];
		min_perimeter = min(min_perimeter, 2*(abs(max_y-min_y)+abs(max_x-min_x)));
	}
	
	cout << min_perimeter << '\n';

	return 0;
}