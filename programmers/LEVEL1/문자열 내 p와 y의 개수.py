'''
https://programmers.co.kr/learn/courses/30/lessons/12916
'''

def solution(s):
    s = s.lower()
    answer = True
    s_dict = {'p' : 0, 'y' : 0}
    for i in s :
        if i in ['p', 'y'] :
            s_dict[i] += 1
    if s_dict['p'] == s_dict['y'] :
        return True
    else :
        return False