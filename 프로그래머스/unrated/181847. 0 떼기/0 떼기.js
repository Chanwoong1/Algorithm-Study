function solution(n_str) {
    var answer = '';
    var b = true
    for (var i = 0; i < n_str.length; i++) {
        if (b && n_str[i] === '0') continue;
        else if (b && n_str[i] !== '0') {
            b = false;
            answer += n_str[i];
        } else answer += n_str[i];
    }
    return answer;
}