n = int(input())

money_list = list(map(int , input().split()))

money_list.sort()
money_list.reverse()
count = 0
for i in money_list:
    count += n // i
    n = n // i
    
print(count)