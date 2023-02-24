def solution(s):
    st = []
    idx = 0
    while idx < len(s) :
        st.append(s[idx])
        if len(st) >= 2 :
            tmp1 = st.pop()
            tmp2 = st.pop()
            if (tmp2 == '(' and tmp1 == ')') == False :
                st.append(tmp2)
                st.append(tmp1)
        idx += 1
    if (len(st) == 0) :
        return True
    else :
        return False