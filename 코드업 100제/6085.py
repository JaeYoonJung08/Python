a, b, c = map(int, input().split())
round = (a * b * c) / 8 /1024 /1024
print(format(round, ".2f"), "MB")