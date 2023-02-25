def solution(survey, choices):
    answer = ''
    rt, cf, jm, an = 0, 0, 0, 0
    for i in range(len(survey)) :
        if (survey[i] == "AN") :
            an += choices[i] - 4
        elif (survey[i] == "NA") :
            an -= (choices[i] - 4)
        elif (survey[i] == "RT") :
            rt += (choices[i] - 4)
        elif (survey[i] == "TR") :
            rt -= (choices[i] - 4)
        elif (survey[i] == "CF") :
            cf += (choices[i] - 4)
        elif (survey[i] == "FC") :
            cf -= (choices[i] - 4)
        elif (survey[i] == "JM") :
            jm += (choices[i] - 4)
        else :
            jm -= (choices[i] - 4)
    answer += "T" if rt > 0 else "R"
    answer += "F" if cf > 0 else "C"
    answer += "M" if jm > 0 else "J"
    answer += "N" if an > 0 else "A"
    return answer