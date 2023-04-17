size, plus_count, dup = map(int , input().split())
number_list = list(map(int , input().split()))

number_list.sort()
first = number_list[size - 1]
second = number_list[size - 2]

result = 0
while True:
    for i in range(dup):
        if (plus_count == 0):
            break
        result += first
        plus_count -= 1
    if (plus_count == 0):
        break
    result += second
    plus_count -= 1
print(result)        
         
        