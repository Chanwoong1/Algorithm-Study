n = [int(i) for i in list(input())]
if len(n) == 1 :
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
    exit(0)
a = n[0] - n[1]
for i in range(1, len(n) - 1) :
    if n[i] - n[i + 1] != a :
        print("흥칫뿡!! <(￣ ﹌ ￣)>")
        exit(0)
print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
