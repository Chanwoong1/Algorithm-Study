def solution(id_pw, db):
    answer = 'fail'
    for info in db :
        if info[0] == id_pw[0] :
            answer = 'wrong pw'
            if info[1] == id_pw[1] :
                answer = 'login'
    return answer