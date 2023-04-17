import re

code = ""
while True:
    try:
        s = input() + "\n"
        code += s
    except:
        while code.find("BUG") != -1:
            code = re.sub("BUG", "", code)
        print(code)
        break
