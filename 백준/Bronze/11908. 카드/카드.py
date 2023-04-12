n = int(input())
cards = [*map(int, input().split())]
print(sum(cards) - max(cards))
