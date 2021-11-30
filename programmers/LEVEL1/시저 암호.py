'''
https://programmers.co.kr/learn/courses/30/lessons/12926
'''

def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():  # 대문자일 경우
            s[i] = chr((ord(s[i]) - ord('A') + n) %26 + ord('A'))   #아스키코드로 변환 후 n만큼 옮겨주고 알파벳으로 다시 변환
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) %26 + ord('a'))

    return "".join(s)