n = int(input())

first = list((map(int, input().split())))
second = list((map(int, input().split())))


result = 0
first.sort()


for i in range(n):
    x = first[i]
    y = max(second)
    result += x * y
    second.pop(second.index(max(second)))  

print(result)