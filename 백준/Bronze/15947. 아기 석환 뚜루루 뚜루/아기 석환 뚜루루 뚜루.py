lst = [
    "baby",
    "sukhwan",
    "tururu",
    "turu",
    "very",
    "cute",
    "tururu",
    "turu",
    "in",
    "bed",
    "tururu",
    "turu",
    "baby",
    "sukhwan",
]
N = int(input())
if (N - 1) % 14 in [2, 3, 6, 7, 10, 11]:
    if (N - 1) // 14 >= 3 and (N - 1) % 14 in [2, 6, 10]:
        print("tu+ru*" + str(2 + (N - 1) // 14))
    elif (N - 1) // 14 >= 4 and (N - 1) % 14 in [3, 7, 11]:
        print("tu+ru*" + str(1 + (N - 1) // 14))
    else:
        print(lst[(N - 1) % 14] + "ru" * ((N - 1) // 14))
else:
    print(lst[(N - 1) % 14])
