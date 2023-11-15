function solution(n) {
    var answer = [];
    for (var i = 0; i < n; i++) {
        answer.push([...Array.from({length:i}, () => 0), 1, ...Array.from({length: n - i - 1}, () => 0)]);
    }
    return answer;
}