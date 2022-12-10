def solution(lines):
    graph = [0] * 200
    for line in lines :
        start, end = line[0], line[1] - 1
        for i in range(start + 100, end + 101) :
            graph[i] += 1
    answer = [1 for i in graph if i > 1]
    return sum(answer)