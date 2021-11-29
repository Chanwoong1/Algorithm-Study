'''
https://programmers.co.kr/learn/courses/30/lessons/72410#
'''

alpha = [i for i in 'abcdefghijklmnopqrstuvwxyz.-_0123456789']

def solution(new_id):
    # 1 stage
    new_id_1 = new_id.lower()
    # 2 stage
    new_id_2 = [i for i in new_id_1 if i in alpha]
    # 3 stage
    for i in range(len(new_id_2) - 1) :
        j = i + 1
        if new_id_2[i] in ['.', ''] and new_id_2[j] == '.' :
            new_id_2[j] = ''
    while new_id_2[-1] == '' :
        new_id_2 = new_id_2[ : -1]
    # 4 stage
    if len(new_id_2) == 1 and new_id_2[0] == '.' :
        new_id_3 = ['a']    # 5 stage
    else :
        if new_id_2[0] == '.' :
            new_id_3 = new_id_2[1 :]
        else :
            new_id_3 = new_id_2
        if new_id_3[-1] == '.' :
            new_id_3 = new_id_3[ : -1]
    new_id_3 = [i for i in ''.join([i for i in new_id_3 if i in alpha])]
    # 6 stage
    if len(new_id_3) >= 16 :
        new_id_3 = new_id_3[ : 15]
        if new_id_3[-1] == '.' :
            new_id_3 = new_id_3[ : -1]
    # 7 stage
    if len(new_id_3) <= 2 :
        ap = new_id_3[-1]
        while len(new_id_3) < 3 :
            new_id_3.append(ap)
    new_id_3 = ''.join([i for i in new_id_3 if i in alpha])
    answer = new_id_3
    return answer