# https://www.acmicpc.net/problem/1864

while 1 :
    octopus = input()
    if octopus == '#' :
        break

    octopus_dict =   {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
    res = 0
    for i in range(len(octopus)) :
        res += octopus_dict[octopus[i]] * 8 ** (len(octopus) - i - 1)    
    print(res)