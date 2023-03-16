n = int(input())
number = 1
sum = 0
while True:
    sum += number
    number += 1
    if(sum >= n):
        print(sum)
        break; 
