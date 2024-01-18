#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> bandage, int health, vector<vector<int>> attacks) {
    int currentHealth = health;
    int lastAttackTime = -1;
    for (auto attack : attacks) {
        if (lastAttackTime != -1) {
            int timeInterval = attack[0] - lastAttackTime - 1;
            if (timeInterval >= bandage[0]) {
                int t = timeInterval / bandage[0];
                int tt = timeInterval % bandage[0];
                cout << "timeInterval: " << timeInterval << ", t: " << t << ", tt: " << tt << ", ";
                currentHealth = min(health, currentHealth + ((bandage[0] * bandage[1] + bandage[2]) * t + bandage[1] * tt));
            } else {
                currentHealth = min(health, currentHealth + (bandage[1] * timeInterval));
            }
        }
        lastAttackTime = attack[0];
        currentHealth -= attack[1];
        if (currentHealth <= 0) break;
        cout << "lastAttackTime: " << lastAttackTime << ", currentHealth: " << currentHealth << "\n";
    }
    return currentHealth > 0 ? currentHealth : -1;
}