# n = int(input())

# flower_count= []

# for i in range(n):
#     temp = list(map(int, input().split()))
#     flower_count.append([temp[0] * 100 + temp[1], temp[2] * 100 + temp[3]])
    
# flower_count.sort(key= lambda x: (x[0]))
# print(flower_count)
# #print(flower_count[0])
# print(len(flower_count))


import sys

n = int(sys.stdin.readline())
date = []

# 편의를 위해 100을 곱해 날짜 형식으로 바꿈
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    date.append([temp[0] * 100 + temp[1], temp[2] * 100 + temp[3]])

# 꽃이 피고 지는 날짜를 오름차순으로 정렬
date.sort(key=lambda x:(x[0], x[1]))
# 선택한 꽃의 개수
#print(date)
cnt = 0
# 제일 늦게 지는 꽃을 비교
end = 0
# 마지막 꽃의 지는 날
target = 301

# 모든 꽃이 없어질 때까지 반복하여 꽃을 비교한다.
while date:
    if target >= 1201 or target < date[0][0]:
        break
    for _ in range(len(date)):
        if target >= date[0][0]:
            if end <= date[0][1]:
                end = date[0][1]
            #print("target, end, data[0][0], data[0][1]", target, end, date[0][0], date[0][1])
            date.remove(date[0])
        else:
            break

    target = end    
    #print("ch target", target)
    cnt += 1
if target < 1201:
    print(0)
else:
    print(cnt)
