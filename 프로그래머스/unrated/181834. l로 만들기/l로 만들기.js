function solution(myString) {
    var answer = '';
    for (var i = 0; i < myString.length; i++) answer += myString[i] <= 'l' ? 'l' : myString[i]; 
    return answer;
}