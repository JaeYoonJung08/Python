a, b, c ,d = map(int, input().split())
round = (a * b *c * d) / 8 /1024 /1024
print(format(round, ".1f"), "MB")