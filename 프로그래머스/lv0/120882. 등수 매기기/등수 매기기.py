def solution(score):
    dict, avg_list = {}, [sum(num) / 2 for num in score]
    for index, avg in enumerate(sorted(avg_list, reverse=True), start=1):
        if avg not in dict:
            dict[avg] = index

    return [dict[avg] for avg in avg_list]