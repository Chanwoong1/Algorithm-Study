function solution(arr) {
    var answer = arr;
    var row = arr.length;
    var col = arr.at(0).length;
    if (row < col) {
        for (var i = 0; i < col - row; i++) answer.push(Array.from({length: col}, () => 0));
    } else {
        for (var i = 0; i < row; i++) answer[i] = answer[i].concat(Array.from({length: row - col}, () => 0));
    }
    return answer;
}