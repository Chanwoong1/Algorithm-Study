#include<string>
#include <iostream>
#include <stack>
using namespace std;

bool solution(string s)
{
    stack<char> st;
    int i = 0;
    while (i < s.length()) {
        st.push(s[i]);
        if (st.size() >= 2) {
            char tmp1, tmp2;
            tmp1 = st.top();
            st.pop();
            tmp2 = st.top();
            st.pop();
            if (!(tmp2 == '(' && tmp1 == ')')) {
                st.push(tmp2);
                st.push(tmp1);
            }
        }
        i++;
    }
    return st.empty();
}