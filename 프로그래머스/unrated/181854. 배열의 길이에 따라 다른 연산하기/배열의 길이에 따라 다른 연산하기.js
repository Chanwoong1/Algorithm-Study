function solution(arr, n) {
    var answer = arr;
    for (var i = arr.length % 2 === 0 ? 1 : 0; i < arr.length; i += 2) answer[i] += n;
    return answer;
}