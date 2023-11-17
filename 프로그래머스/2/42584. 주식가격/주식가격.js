function solution(prices) {
    var stack = [];
    var answer = new Array(prices.length).fill(-1);
    var time = 0;
    for (var i = 0; i < prices.length; i++, time++) {
        while (stack.length && stack[stack.length - 1][0] > prices[i]) {
            answer[stack[stack.length - 1][1]] = time - stack[stack.length - 1][1];
            stack.pop();
        }
        stack.push([prices[i], time]);
    }
    for (var [_, t] of stack) answer[t] = time - t - 1;
    return answer;
}