K = int(input())
lst = [input() for _ in range(int(input()))]
time = 0
for i in lst :
    T, Z = i.split()
    if Z == "T" :
        if time + int(T) < 210 :
            time += int(T)
            K += 1
            if K == 9 : K = 1
        else :
            print(K)
            break
    else :
        time += int(T)
        if time >= 210 :
            print(K)
            break
