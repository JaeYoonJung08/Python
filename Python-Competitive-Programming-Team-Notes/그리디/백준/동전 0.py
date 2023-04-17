count, money = map(int, input().split())

money_list = []
for i in range(count):
    money_count = int(input())
    money_list.append(money_count)

money_list.sort()
money_list.reverse()
answer = 0

compare = money
for i in money_list:
    if (compare % i >= compare):
        #print(i)
        continue
    answer += money // i
    money = money % i
    if (money == 0):
        break
    #print(money)
    #print(money)
print(answer)