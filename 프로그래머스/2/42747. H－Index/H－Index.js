function solution(citations) {
    var answer = 0;
    let arr = [];
    citations = citations.sort((a,b) => b - a);
    for (let citation of citations) {
        arr.push(citation);
        if (citation < arr.length) break;
        answer++;
    }
    return answer;
}