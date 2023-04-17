

# import sys
# input = sys.stdin.readline

N = int(input())
table = []
for i in range(N):
    s,e = map(int, input().split())
    table.append((s,e))

count = 0 #회의 개수
cur_end = 0 #현재까지 종료시간

#시작시간으로 오름차순 -> 종료시간으로 오름차순
table.sort(key=lambda a: a[0])
table.sort(key=lambda a: a[1])

print(table)
for S,E in table:
    if S >= cur_end:
        cur_end = E
        count += 1
        print("S E", S, E)

print(count)



# #inpit = input().split()
# n = int(input())

# check_time = []

# for i in range(n):
#     first_time, second_tme = map(int, input().split())
#     check_time.append((first_time, second_tme))

# count = 0
# check_index = 0

# check_time.sort(key=lambda a: a[0])
# print("1", check_time)
# check_time.sort(key=lambda a: a[1])
# print("2", check_time)
# second = 0
# for i in range(0, n):
#     if (check_time[i][0] >= second):
#         count += 1
#         second = check_time[i][1]
#         print(second)
#         #print(check_time[check_index][0], check_time[check_index][1])
#     #print(i)
#     # if (check_index == n - 1):
#     #     break
    
# #print( check_time[check_index][0])

# print(count)

