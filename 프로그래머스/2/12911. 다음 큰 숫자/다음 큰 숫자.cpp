#include <bitset>
#include <string>

using namespace std;

int countOnes(int number) {
    return bitset<32>(number).count();
}

int solution(int n) {
    int originalOnes = countOnes(n);
    for (int next = n + 1; next <= 1000000; ++next) {
        if (countOnes(next) == originalOnes) {
            return next;
        }
    }
    return -1;
}