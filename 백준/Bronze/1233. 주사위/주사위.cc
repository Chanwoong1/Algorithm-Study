#include <iostream>
#include <cstring>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0), cout.tie(0);
	int S1, S2, S3;
	cin >> S1 >> S2 >> S3;
	int arr[S1 + S2 + S3 + 1];
	memset(arr, 0, sizeof(int) * (S1 + S2 + S3 + 1));
	for (int i = 1; i < S1 + 1; ++i)
		for (int j = 1; j < S2 + 1; ++j)
			for (int k = 1; k < S3 + 1; ++k)
				++arr[i + j + k];
	int idx = 0;
	int max = arr[0];
	for (int i = 0; i < S1 + S2 + S3 + 1; ++i) {
		if (arr[i] > max) {
			idx = i;
			max = arr[i];
		}
	}
	cout << idx << "\n";
}
